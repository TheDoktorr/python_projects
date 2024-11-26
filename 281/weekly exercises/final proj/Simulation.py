import numpy as np
from Particle import Particle
from InitCon import *
import copy

iterations = 2000
time = 0 
deltaT = 6
Data = []
bodies = [Earth, Satellite]



# print results
with open("281/weekly exercises/final proj/output.txt", "w") as f:

        # loop for Euler method
    for i in range(iterations):
            
        for particle in bodies:
            particle.updateGravaccel(bodies)
            particle.updateE(deltaT)
            
        time += deltaT
     
    print("The Earth and Satellite's locations after {0} seconds using:".format((2000*6)), file=f)
    for particle in [Earth, Satellite]:
        print("  Particle: {}".format(particle.name), file=f)
        print("    Mass: {0:.3e}, ".format(particle.mass), file=f)
        for attribute in ["position", "velocity", "acceleration"]:
            print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0), file=f)  # add 0.0 to avoid negative zeros!


    # same loop applied to Euler-Cromer
    for i in range(iterations):
            
        for particle in bodies:
            particle.updateGravaccel(bodies)
            particle.updateEC(deltaT)
            
        time += deltaT


     
    print("The Earth and Satellite's locations after {0} seconds using:".format((2000*6)), file=f)
    for particle in [Earth, Satellite]:
        print("  Particle: {}".format(particle.name), file=f)
        print("    Mass: {0:.3e}, ".format(particle.mass), file=f)
        for attribute in ["position", "velocity", "acceleration"]:
            print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0), file=f)  # add 0.0 to avoid negative zeros!
