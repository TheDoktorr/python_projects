import numpy as np
from Particle import Particle
from InitCon import *
import copy

iterations = 2000
time = 0 
deltaT = 6
Data = []
bodies = [Earth, Satellite, Satellite2]

 # initialisation string 
print("What Method would you like to use, Euler (1), Euler-Cromer (2)  or ")
method = int(input())
if not isinstance(method, (int)):
    raise ValueError("This is not an option")
if method > 3:
    raise ValueError("This is not one of the options!")



# print results
with open("281/weekly exercises/final proj/output.txt", "w") as f:
    
        # loop for Euler method
    for i in range(iterations):
            
        for particle in bodies:
            particle.updateGravaccel(bodies)

            if method == 1:
                particle.updateE(deltaT)
            elif method == 2:
                particle.updateEC(deltaT)
            
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

