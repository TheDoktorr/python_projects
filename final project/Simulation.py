import numpy as np
import copy
import matplotlib.pyplot as plt

from Particle import Particle
from Graphs import *
from Setup import *

    

# iterations = Total Time/deltaT

time = 0 
deltaT = 3600
iterations = 10000
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
            
    for particle in bodies:
        particle.updateGravaccel(bodies)

        if method == 1:
            particle.updateE(deltaT)
        elif method == 2:
            particle.updateEC(deltaT)
        
                    
    time += deltaT


    for particle in bodies:

        xpos[particle.name].append(particle.position[0])
        ypos[particle.name].append(particle.position[1])
        zpos[particle.name].append(particle.position[2])
        # Accumulate total energy

  
    timeLog.append(time)
    print(f"Iteration {i}")
    total_linearMom = sum(p.linearMomentum() for p in bodies)
    linearMom.append(np.linalg.norm(total_linearMom))

    # Calculate total energy and momentum
    total_energy = 0.0
    #total_momentum = np.array([0.0, 0.0, 0.0])
    total_ang_mom = np.array([0.0, 0.0, 0.0])
    for particle in bodies:
        total_energy += particle.kineticEnergy() + 0.5 * particle.potentialEnergy(bodies)
        print(particle.mass)
        print(particle.velocity)
        # Accumulate total momentum vector
        
        total_ang_mom += particle.angularMomentum()



    # Calculate magnitude of the total momentum vector
  
    total_ang_mom_mag = np.linalg.norm(total_ang_mom)

    # Store results
    totalEnergy.append(total_energy)
    
    angularMom.append(total_ang_mom_mag)


orbits2D()
orbits3D()
EnergyCons()
LinearMomCons()
AngMomCons()

"""
list to do:
linear momentum - CONVSERED
keplers laws
angular kinetic  - probs not
angular momentum
verlet
graphs
user input
"""