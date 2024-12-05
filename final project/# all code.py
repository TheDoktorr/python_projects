# all code

import numpy as np
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from astropy.constants import G
from spiceypy import sxform, mxvg
from poliastro import constants
import matplotlib.pyplot as plt


class Particle:
    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, -10, 0], dtype=float),
        name="point particle",
        mass=1.0,
        G=6.67408E-11,
    ):
        # Ensure all attributes are copied and cast to np.float64
        self.position = np.array(np.copy(position), dtype=np.float64)
        self.velocity = np.array(np.copy(velocity), dtype=np.float64)
        self.acceleration = np.array(np.copy(acceleration), dtype=np.float64)
        self.name = name
        self.mass = np.float64(mass)
        self.G = np.float64(G)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def updateE(self, deltaT):
        """
        Update position and velocity based on the Euler Method
        takes self.position, velocity, acceleration as passed to it
        takes deltaT as the time step of the update
        """
        self.deltaT = deltaT
        self.position = np.float64(self.position) + np.float64(self.velocity) * np.float64(deltaT)
        self.velocity = np.float64(self.velocity) + np.float64(self.acceleration) * np.float64(deltaT)


    
    def updateEC(self, deltaT):
        """
        Alternative method for updating based on Euler-Cromer method 
        
        """
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT




    def updateGravitationalAcceleration(self, body):
        distance = np.float64(np.linalg.norm(self.position - body.position))
        if distance == 0:
            return np.array([0.0, 0.0, 0.0], dtype=np.float64)

        gravaccel = -np.float64(self.G * body.mass) * (self.position - body.position) / (distance**3)
        self.acceleration = np.array(gravaccel, dtype=np.float64)
        return gravaccel

    def updateGravaccel(self, bodies):
        total_gravaccel = np.array([0.0, 0.0, 0.0], dtype=np.float64)
        for body in bodies:
            if body is not self:
                distance = np.float64(np.linalg.norm(self.position - body.position))
                if distance < 1e-20:  # Threshold to treat as zero
                    gravaccel = np.array([0.0, 0.0, 0.0])
                else:
                    gravaccel = - (self.G * body.mass) * (self.position - body.position) / (distance**3)
                total_gravaccel += np.array(gravaccel, dtype=np.float64)

        self.acceleration = np.array(total_gravaccel, dtype=np.float64)
            
        

    def kineticEnergy(self):
        Kvelocity = np.float64(np.linalg.norm(self.velocity))
        Kenergy = np.float64(0.5) * self.mass * Kvelocity**2
        return np.float64(Kenergy)

    def potentialEnergy(self, bodies):
        potentialE = np.float64(0.0)
        for body in bodies:
            if body is not self:
                distance = np.float64(np.linalg.norm(self.position - body.position))
                if distance < 1e-25:
                    distance += np.float64(1e-10)

                U = -np.float64(self.G * self.mass * body.mass) / distance
                potentialE += np.float64(U)

        return np.float64(potentialE)


        
    
    def linearMomentum(self):
        clm = np.array([0.0, 0.0, 0.0])
        
        linear_Momentum = self.mass * self.velocity
        clm += linear_Momentum
        return clm
    
    def angularMomentum(self):

        return np.cross(self.position, (self.mass * self.velocity))

    def masscaller(self):
        return self.mass
    



 # Using Astropy, we import the time
t = Time("2024-11-26 17:00:00.0", scale="tdb")

# we now get the positions and velocities of solar system bodies
def coord_conv(body):
    pos, vel = get_body_barycentric_posvel(body, t, ephemeris="jpl")
    statevec = [
        np.float64(pos.xyz[0].to("m").value),
        np.float64(pos.xyz[1].to("m").value),
        np.float64(pos.xyz[2].to("m").value),
        np.float64(vel.xyz[0].to("m/s").value),
        np.float64(vel.xyz[1].to("m/s").value),
        np.float64(vel.xyz[2].to("m/s").value),
    ]

    trans = sxform("J2000", "ECLIPJ2000", t.jd)
    statevececl = mxvg(trans, statevec)

    new_position = np.array(statevececl[:3], dtype=np.float64)
    new_velocity = np.array(statevececl[3:], dtype=np.float64)

    return new_position, new_velocity


# function to change input to uppercase, to work with variable names
def UpperCase(lower):
    lowertxt = str(lower)
    lowertxt = lowertxt.capitalize()
    return lowertxt

# function to make word lowercase, as JPL names are all lowercase    
def LowerCase(Upper):
    Uppertxt = str(Upper)
    Uppertxt = Uppertxt.lower()
    return Uppertxt


# dictionary reference of mass constants for ClassMaker to reference
GM_constants = {
    "sun": constants.GM_sun,
    "mercury": constants.GM_mercury,
    "venus": constants.GM_venus,
    "earth": constants.GM_earth,
    "mars": constants.GM_mars,
    "jupiter": constants.GM_jupiter,
    "saturn": constants.GM_saturn,
    "uranus": constants.GM_uranus,
    "neptune": constants.GM_neptune


}

def massFunc(body_input):
        if body_input in GM_constants:
            GM_input = GM_constants[body_input]
            return np.float64((GM_input / G).value)
        else:
            raise ValueError("No mass found for that body")


def ClassMaker(body_input):
    body_input_l = LowerCase(body_input)
    body_input_U = UpperCase(body_input)

    body = Particle(
        position=np.array(coord_conv(body_input_l)[0], dtype=np.float64),
        velocity=np.array(coord_conv(body_input_l)[1], dtype=np.float64),
        acceleration=np.array([0, 0, 0], dtype=np.float64),
        name=body_input_U,
        mass=np.float64(massFunc(body_input_l)),
    )
    return body


# planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets = ["Sun", "Mercury", "Venus", "Earth"]
# planets = ["Sun", "Earth"]
bodies = []


for i in range(len(planets)):       # for each planet
    
    body = ClassMaker(planets[i])   # make a class associated with it
    bodies.append(body)             # add to list
    
# setup body coordinate lists, as blank lists
xpos = {particle.name: [] for particle in bodies}   
ypos = {particle.name: [] for particle in bodies}
zpos = {particle.name: [] for particle in bodies}


#time and energy for logging and graphing
timeLog = []
linearMom = [] 
angularMom =[]
totalEnergy = []






# iterations = Total Time/deltaT

time = 0 
deltaT = 3600
iterations = int(31_557_600 / deltaT)
#int(31_557_600 / deltaT)

 # initialisation string 
print("What Method would you like to use, Euler (1), Euler-Cromer (2)  or ")
method = int(input())
if not isinstance(method, (int)):
    raise ValueError("This is not an option")
if method > 3:
    raise ValueError("This is not one of the options!")




    
# main simulation loop

for i in range(iterations):

    timeLog.append(time)
    print(f"Iteration {i}")
    # init total energy and momentum
    
    total_momentum = np.array([0.0, 0.0, 0.0])

    for particle in bodies:
        
        particle.updateGravaccel(bodies)

        if method == 1:
            particle.updateE(deltaT)
        elif method == 2:
            particle.updateEC(deltaT)
        
        xpos[particle.name].append(np.float64(particle.position[0]))
        ypos[particle.name].append(np.float64(particle.position[1]))
        zpos[particle.name].append(np.float64(particle.position[2]))
                
        
    time += deltaT
    
    total_momentum = np.sum([np.float64(particle.mass) * particle.velocity for particle in bodies], axis=0)
    momentum_norm = np.float64(np.linalg.norm(total_momentum))
    linearMom.append(momentum_norm)
   

    angularMomentum = np.sum([np.float64(particle.angularMomentum()) for particle in bodies], axis=0)
    angularMom.append(np.float64(np.linalg.norm(angularMomentum)))

    total_energy = np.float64(0.0)
    for p in bodies:
        total_energy += np.float64(p.kineticEnergy() + 0.5 * p.potentialEnergy(bodies))
    totalEnergy.append(np.float64(total_energy))
    



linearMom.sort()
print(linearMom[0], linearMom[-1])


def LinearMomCons():
    fig=plt.figure(dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$ (kg ms^{-1})$')
    
    ax.plot(timeLog, linearMom, label="CLM", lw=1)

    ax.legend()
    fig.tight_layout()
    plt.show()

    

def EnergyCons():
    fig=plt.figure(figsize=(3.5,2.6),dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$E$ (J)')

    ax.plot(timeLog, totalEnergy, label="Total Energy", lw=0.4)

    ax.legend()
    plt.savefig("EnergyConsV.svg")
    plt.show()

EnergyCons()

LinearMomCons()
linearMom.sort()
print(linearMom[0], linearMom[-1])

totalEnergy.sort()
print(totalEnergy[0],totalEnergy[1])
angularMom.sort()
print(angularMom[0], angularMom[1])

