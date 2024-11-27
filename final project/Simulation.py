import numpy as np
import copy
import matplotlib.pyplot as plt

from Particle import Particle
from InitCon import *


iterations = 2000
time = 0 
deltaT = 500
Data = []
bodies = [earth, sun]

 # initialisation string 
print("What Method would you like to use, Euler (1), Euler-Cromer (2)  or ")
method = int(input())
if not isinstance(method, (int)):
    raise ValueError("This is not an option")
if method > 3:
    raise ValueError("This is not one of the options!")



# print results
with open(r"final project\output.txt", "w") as f:
    
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
           #  for particle in bodies:
           # Data.append([time, copy.deepcopy(earth), copy.deepcopy(sun)])
           # print("    {}: {}".format("position", particle.__getattribute__("position") + 0.0), file=f)
                positions = [particle.position for particle in bodies]
                Data.append(positions)

                

   
    
    print("The Earth and Satellite's locations after {0} seconds using:".format((2000*6)), file=f)
    for particle in  bodies:
        print("  Particle: {}".format(particle.name), file=f)
        print("    Mass: {0:.3e}, ".format(particle.mass), file=f)
        for attribute in ["position", "velocity", "acceleration"]:
            print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0), file=f)  # add 0.0 to avoid negative zeros!


    print(Data, file=f)
    Data_array = np.array(Data)
    print(Data_array, file=f)
 
"""
fig=plt.figure(figsize=(3.5,2.6),dpi=200)
ax=fig.add_subplot(1,1,1)
ax.set_xlabel(r'$x$ (m)')
ax.set_ylabel(r'$y$ (m)')
xx=np.arange(-3.0,3.0,0.1)  # Array of x values to plot.
yy=self.U(xx) # Function U can take a NumPy array xx and return an array of corresponding potential values.
ax.plot(xx,UU,label="anharmonic")
UU=0.5*self.k*xx**2 # Harmonic potential values, for comparison.
ax.plot(xx,UU,label="harmonic")
ax.legend()
fig.tight_layout()
plt.show()
"""