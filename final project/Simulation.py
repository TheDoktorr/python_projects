import numpy as np
import copy
import matplotlib.pyplot as plt

from Particle import Particle
from Graphs import *
from Setup import *

    

# iterations = Total Time/deltaT

time = 0 
deltaT = 3600
iterations = 2000000
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
  #  if i % 1000 == 0:

    for particle in bodies:

        xpos[particle.name].append(particle.position[0])
        ypos[particle.name].append(particle.position[1])
        zpos[particle.name].append(particle.position[2])
  #  if i % 1000 == 0:
    timeLog.append(time)

        # Calculate total energy and momentum
    total_energy = 0.0
    total_momentum = np.array([0.0, 0.0, 0.0])

    # Loop through particles
    for p in bodies:
            # Accumulate total energy
        total_energy += p.kineticEnergy() + 0.5 * p.potentialEnergy(bodies)

            # Accumulate total momentum vector
        total_momentum += p.linearMomentum()

        # Calculate magnitude of the total momentum vector
    total_momentum_magnitude = np.linalg.norm(total_momentum)
    print(f"Iteration {i}")

        # Store results
    totalEnergy.append(total_energy)
    linearMom.append(total_momentum_magnitude)



orbits2D()
orbits3D()
EnergyCons()
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