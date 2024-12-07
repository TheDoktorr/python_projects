from os import path

# test code 1



from Simulation import *
print("The Earth and Satellite's locations after {0} seconds are:".format((2000*6)))
for particle in [Earth, Satellite]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


# test code 2


def print_particle(particle):
    print("Particle: {}".format(particle.name))
    print("  Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


print("The Earth and Satellites Location after {0} seconds is:".format((2000*6)))
print_particle(Earth)
print_particle(Satellite)
if path.exists("TwoBodyTest.npy"):
    print("The file TwoBodyTest.npy has been created.")

print("testing reading it back in")
DataIn = np.load("TwoBodyTest.npy", allow_pickle=True)

print("Printing First Entry")
print("{}".format(int(DataIn[0][0])))  #time
print_particle(DataIn[0][1])  # Earth
print_particle(DataIn[0][2])  # Satellite

print("Printing Fifth Entry")
print("{}".format(int(DataIn[4][0])))  #time
print_particle(DataIn[4][1])  # Earth
print_particle(DataIn[4][2])  # Satellite

print("Printing Last Entry")
print("{}".format(int(DataIn[-1][0])))  #time
print_particle(DataIn[-1][1])  # Earth
print_particle(DataIn[-1][2])  # Satellite



import numpy as np
from Particle import Particle
import math
Data = np.load("TwoBodyTest.npy", allow_pickle=True)
print(Data[0][1].kineticEnergy())

DataIn = np.load("TwoBodyTest.npy", allow_pickle=True)

def print_particle(particle):
    print("Particle: {}".format(particle.name))
    print("  Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!

print("Testing reading the file TwoBodyTest.npy that you have loaded")

float_formatter = lambda x: "%.5e" % x
np.set_printoptions(formatter={'float_kind': float_formatter})


print("Printing First Entry")
print("{}".format(int(DataIn[0][0])))  #time
print_particle(DataIn[0][1])  # Earth
print_particle(DataIn[0][2])  # Satellite

print("Printing Fifth Entry")
print("{}".format(int(DataIn[4][0])))  #time
print_particle(DataIn[4][1])  # Earth
print_particle(DataIn[4][2])  # Satellite

print("Printing Last Entry")
print("{}".format(int(DataIn[-1][0])))  #time
print_particle(DataIn[-1][1])  # Earth
print_particle(DataIn[-1][2])  # Satellite


print("Testing reading the file TwoBodyTest.npy  that you have loaded")

print("Printing Kinetic Energy of First Entry Earth and Satellite")
print("Earth KE: {:.5e}".format(DataIn[0][1].kineticEnergy()))
print("Satellite KE: {:.5e}".format(DataIn[0][2].kineticEnergy()))

print("Printing Kinetic Energy of Last Entry")
print("Earth KE: {:.5e}".format(DataIn[-1][1].kineticEnergy()))
print("Satellite KE: {:.5e}".format(DataIn[-1][2].kineticEnergy()))



# original iteration loop for Euler method
for i in range(iterations):
        Satellite.updateGravitationalAcceleration(Earth)
        Earth.updateGravitationalAcceleration(Satellite)
        Satellite.updateE(deltaT)
        Earth.updateE(deltaT)
        time += deltaT

        if i % 100 == 0:
                Data.append([time, copy.deepcopy(Earth), copy.deepcopy(Satellite)])

# np.save(r"281\weekly exercises\final proj\TwoBodyTest.npy", Data, allow_pickle=True)  

   # original iteration loop for Euler method
    for i in range(iterations):

            Satellite.updateGravitationalAcceleration(Earth)
            Earth.updateGravitationalAcceleration(Satellite)
            Satellite.updateE(deltaT)
            Earth.updateE(deltaT)
            time += deltaT

            if i % 100 == 0:
                   Data.append([time, copy.deepcopy(Earth), copy.deepcopy(Satellite)])

    # np.save(r"281\weekly exercises\final proj\TwoBodyTest.npy", Data, allow_pickle=True)  
    
    print("The Earth and Satellite's locations after {0} seconds using:".format((2000*6)), file=f)
    for particle in [Earth, Satellite]:
        print("  Particle: {}".format(particle.name), file=f)
        print("    Mass: {0:.3e}, ".format(particle.mass), file=f)
        for attribute in ["position", "velocity", "acceleration"]:
            print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0), file=f)  # add 0.0 to avoid negative zeros!

            
            
           # Data.append([time, copy.deepcopy(earth), copy.deepcopy(sun)])
           # print("    {}: {}".format("position", particle.__getattribute__("position") + 0.0), file=f)



               
                current_positions = [body.position for body in bodies]  # List of positions at this timestep
                positions_over_time.append(current_positions) 
                positions_array = np.array(positions_over_time)  # Convert to NumPy array for easier slicing

                for i, body in enumerate(bodies):  # Loop over all bodies
                    plt.plot(positions_array[:, i, 0], positions_array[:, i, 1], label=body.name)
                

# print results
 with open(r"final project\output.txt", "w") as f:  

 """
Earth = Particle(
    position=np.array(coord_conv("earth")[0]),
    velocity=np.array(coord_conv("earth")[1]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass = Earth_m
)

Sun = Particle(
    position=np.array(coord_conv("sun")[0]),
    velocity=np.array(coord_conv("sun")[1]),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass = Sun_m
)
"""


 
print("The Earth and Sateforllite's locations after {0} seconds using:".format((2000*6)))
for particle in  bodies:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!

earthMass = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass
)

satPosition = earthRadius + (35786 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite = Particle(
    position=np.array([satPosition, 0, 0]),
    velocity=np.array([0, satVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=100.
)

satPosition = earthRadius + (35992 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite2 = Particle(
    position=np.array([satPosition, 0, 0]),
    velocity=np.array([0, satVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=150.
)
xx = xpos[name] / 149597870700
        yy = ypos[name] / 149597870700
        zz = zpos[name] / 149597870700



"""
linearMom = np.array(linearMom)
plt.figure(figsize=(10, 6))
plt.plot(timeLog, linearMom[:, 0], label="Px")  # x-component

plt.ylabel("Momentum Components")
plt.title("Momentum Components Over Time")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(timeLog, linearMom[:, 1], label="Py")  # y-component

plt.xlabel("Time")
plt.ylabel("Momentum Components")
plt.title("Momentum Components Over Time")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(timeLog, linearMom[:, 2], label="Pz")  # z-component
plt.xlabel("Time")
plt.ylabel("Momentum Components")
plt.title("Momentum Components Over Time")
plt.legend()
plt.grid()
plt.show()
"""




plt.figure(figsize=(10, 6))
plt.plot(timeLog, linearMom[:, 0], label="Px")  # x-component

plt.ylabel("Momentum Components")
plt.title("Momentum Components Over Time")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(timeLog, linearMom[:, 1], label="Py")  # y-component

plt.xlabel("Time")
plt.ylabel("Momentum Components")
plt.title("Momentum Components Over Time")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(timeLog, linearMom[:, 2], label="Pz")  # z-component
plt.xlabel("Time")
plt.ylabel("Momentum Components")
plt.title("Momentum Components Over Time")
plt.legend()
plt.grid()
plt.show()

verlet

        #accelN1 = np.array([0.0, 0.0, 0.0])
        self.position = self.position + self.velocity*deltaT + 0.5*self.acceleration*(deltaT)**2
        est = copy.deepcopy(self)
        bodiesN = copy.deepcopy(bodies)
        est.updateGravaccel(bodiesN)

        self.velocity = self.velocity + 0.5*(est.acceleration + self.acceleration)*deltaT
        self.updateGravaccel(bodies)




        i =0
        estimatedbodies = [np.zeros(3, dtype=np.float64) for j in range(len(bodies))]
        for body in bodies:
            body.position = body.position + body.velocity*deltaT + 0.5*body.acceleration*(deltaT)**2
            i += 1
        estimatedbodies[i] = copy.deepcopy(body)

        bodiescopy = copy.deepcopy(estimatedbodies)
        i = 0
        for body in bodies:
            estimatedbodies[i].updateGravaccel(bodiescopy)
            i += 1

        i=0
        for body in bodies:
            body.velocity = body.velocity + 0.5*(estimatedbodies[i].acceleration + body.acceleration)*deltaT
            i += 1


    """
    kinetic_energy = sum(body.kineticEnergy() for body in bodies)
    potential_energy = sum(0.5 * body.potentialEnergy(bodies) for body in bodies)
    total_energy = kinetic_energy + potential_energy
    totalEnergy.append(np.float64(total_energy))
   
    for k, p1 in enumerate(bodies):
        kinetic_energy += p1.kineticEnergy()  # Kinetic energy for each particle
        for j, p2 in enumerate(bodies):
            if j > k:  # Only calculate potential energy once per pair
                distance = np.linalg.norm(p1.position - p2.position)
                potential_energy += (-p1.G * p1.mass * p2.mass) / (distance)

    total_energy = kinetic_energy + potential_energy
    totalEnergy.append(total_energy)
    """