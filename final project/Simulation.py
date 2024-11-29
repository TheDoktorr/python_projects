import numpy as np
import copy
import matplotlib.pyplot as plt

from Particle import Particle
from Graphs import *
from Setup import *

    


iterations = 100000
time = 0 
deltaT = 500


 # initialisation string 
print("What Method would you like to use, Euler (1), Euler-Cromer (2)  or ")
method = int(input())
if not isinstance(method, (int)):
    raise ValueError("This is not an option")
if method > 3:
    raise ValueError("This is not one of the options!")




    
# main simulation loop

for i in range(iterations):
            
    for particle in bodies:
        particle.updateGravaccel(bodies)

        if method == 1:
            particle.updateE(deltaT)
        elif method == 2:
            particle.updateEC(deltaT)
        
        

            
    time += deltaT
    if i % 100 == 0:

        for particle in bodies:

            xpos[particle.name].append(particle.position[0])
            ypos[particle.name].append(particle.position[1])
            zpos[particle.name].append(particle.position[2])
    if i % 1000 == 0:
            timeLog.append(time)
            totalEnergy.append(particle.kineticEnergy() + 0.5* particle.potentialEnergy(bodies))
            linearMom.append(particle.linearMomentum())



                


# orbits2D()
# orbits3D()
# EnergyCons()
LinearMomCons()
"""
list to do:
linear momentum - CONVSERED
angular kinetic  - probs not
angular momentum
verlet
graphs
user input
"""