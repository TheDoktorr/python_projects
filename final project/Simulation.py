import numpy as np
import copy
import matplotlib.pyplot as plt

from Particle import Particle
from InitCon import *


Sun = ClassMaker("Sun")
Earth = ClassMaker("Earth")
Mercury = ClassMaker("Mercury")
Venus = ClassMaker("Venus")
bodies = [Sun, Earth, Mercury, Venus]

iterations = 100000
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
                
                


 
print("The Earth and Satellite's locations after {0} seconds using:".format((2000*6)))
for particle in  bodies:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!

    
    Earth_xpos = np.array(xpos["Earth"])  # Convert to a numpy array for easier slicing
    Earth_ypos = np.array(ypos["Earth"])
    Sun_xpos = np.array(xpos["Sun"])
    Sun_ypos = np.array(ypos["Sun"])
    Mercury_xpos = np.array(xpos["Mercury"])
    Mercury_ypos = np.array(ypos["Mercury"])
    Venus_xpos = np.array(xpos["Venus"])
    Venus_ypos= np.array(ypos["Venus"])
    
 
 
fig=plt.figure(figsize=(3.5,2.6),dpi=200)
ax=fig.add_subplot(1,1,1)
ax.set_xlabel(r'$x$ (m)')
ax.set_ylabel(r'$y)$ (m)')
ax.plot(Earth_xpos,Earth_ypos,label="Earth", lw=0.4)
ax.plot(Sun_xpos, Sun_ypos, label="Sun", lw=0.4)
ax.plot(Mercury_xpos, Mercury_ypos, label="Mercury", lw=0.4)
ax.plot(Venus_xpos, Venus_ypos, label="Venus", lw=0.4)
ax.legend()
fig.tight_layout()
plt.show()
