import numpy as np
from astropy.constants import G
import copy

class Particle:
    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=np.float64),
        velocity=np.array([0, 0, 0], dtype=np.float64),
        acceleration=np.array([0, -10, 0], dtype=np.float64),
        name="point particle",
        mass=1.0,
        G = G
    ):
        self.position = np.array(np.copy(position), dtype=np.float64)
        self.velocity = np.array(np.copy(velocity), dtype=np.float64)
        self.acceleration = np.array(np.copy(acceleration), dtype=np.float64)
        self.name = name
        self.mass = np.float64(mass)
        self.G = np.float64(G)
        
        
    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
        self.name, self.mass,self.position, self.velocity, self.acceleration
    )

    def updateE(self, deltaT):
        """
        Update position and velocity based on the Euler Method
        takes self.position, velocity, acceleration as passed to it
        takes deltaT as the time step of the update
        """

        self.deltaT = deltaT
        
        self.position = self.position + self.velocity * self.deltaT
        self.velocity = self.velocity  + self.acceleration * self.deltaT

    def updateEC(self, deltaT):
        """
        Alternative method for updating based on Euler-Cromer method 
        
        """

        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT



    def updateGravaccel(self, bodies):
        """
        Method for many body acceleration of bodies 
        list of bodies, e.g [satellite1, satellite2]

        self = i
        bodies = j
        """
        total_gravaccel = np.array([0.0, 0.0, 0.0])
        for body in bodies:
            if body is not self:
               # epsilon = 1e-6
                distance = np.linalg.norm(self.position - body.position)
               # distance = np.sqrt(distance**2 + epsilon**2)
                
                epsilon = 1e-6  # Softening factor
                if distance < 1e-25:
                    distance = np.sqrt(distance**2 + epsilon**2)  # Softened distance

                gravaccel = -np.float64(self.G * body.mass) * (self.position - body.position) / (distance**3)
                total_gravaccel += np.array(gravaccel, dtype=np.float64)

        self.acceleration = np.array(total_gravaccel, dtype=np.float64)
        
    def updateVerlet(self, bodies, deltaT):
        """
        Method for approximating positions and velocities based on accelerations, using end accelerations to update velocity
        This smooths out changes in acceleration
        input also requires bodies to update end acceleration
        """    
   
        i =0
        estimatedbodies = [np.zeros(3, dtype=np.float64) for j in range(len(bodies))]
        for body in bodies:
            body.position = body.position + body.velocity*deltaT + 0.5*body.acceleration*(deltaT)**2
            estimatedbodies[i] = copy.deepcopy(body)
            i += 1
        

        bodiescopy = copy.deepcopy(estimatedbodies)
        i = 0
        for body in bodies:
            estimatedbodies[i].updateGravaccel(bodiescopy)
            i += 1

        i=0
        for body in bodies:
            body.velocity = body.velocity + 0.5*(estimatedbodies[i].acceleration + body.acceleration)*deltaT
            i += 1

    def kineticEnergy(self):
        Kvelocity= np.linalg.norm(self.velocity)

        Kenergy =  0.5 * self.mass * Kvelocity**2

        return Kenergy


    def potentialEnergy(self, bodies):
        potentialE = 0 
        epsilon = 1e-5
        for body in bodies:
            if body is not self:
                distance = np.linalg.norm(self.position - body.position)
                U = ( -self.G * self.mass * body.mass ) / (distance+epsilon)
                potentialE += U
        return potentialE
    
    def linearMomentum(self):
        return self.mass * self.velocity
    
    def angularMomentum(self):
        return np.cross(self.position, (self.mass * self.velocity))

    def masscaller(self):
        return self.mass
    
