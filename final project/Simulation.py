import numpy as np
import copy
import matplotlib.pyplot as plt

from Particle import Particle
from InitCon import *


# planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter"]
bodies = []

for i in range(len(planets)):
    print(planets[i])
    body = ClassMaker(planets[i])
    bodies.append(body)
    





iterations = 1000000
time = 0 
deltaT = 500


# setup body coordinate lists
xpos = {particle.name: [] for particle in bodies}
ypos = {particle.name: [] for particle in bodies}
zpos = {particle.name: [] for particle in bodies}



 # initialisation string 
print("What Method would you like to use, Euler (1), Euler-Cromer (2)  or ")
method = int(input())
if not isinstance(method, (int)):
    raise ValueError("This is not an option")
if method > 3:
    raise ValueError("This is not one of the options!")




    
        # loop for Euler method
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
                
                


 
print("The Earth and Sateforllite's locations after {0} seconds using:".format((2000*6)))
for particle in  bodies:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!




fig=plt.figure(figsize=(3.5,2.6),dpi=200)
ax=fig.add_subplot(1,1,1)
ax.set_xlabel(r'$x$ (m)')
ax.set_ylabel(r'$y$ (m)')

for name in xpos:
    ax.plot(xpos[name], ypos[name], label = name, lw=0.4)
ax.legend()
fig.tight_layout()
plt.show()
