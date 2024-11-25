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
