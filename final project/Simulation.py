import numpy as np
import matplotlib.pyplot as plt #get rid of

from Graphs import *
from Setup import *



# iterations = Total Time/deltaT

time = 0 
deltaT = 60
iterations =int(170 *31_536_000 / deltaT)
#int(1 *31_557_600 / deltaT)

 # initialisation strin2g 
print("What Method would you like to use, Euler (1), Euler-Cromer (2)  or Verlet (3)?")
method = int(input())
if not isinstance(method, (int)):
    raise ValueError("This is not an option")
if method > 3:
    raise ValueError("This is not one of the options!")


    
# main simulation loop

for i in range(iterations):
    
    timeLog.append(time)
    # print(f"Iteration {i}")
    # init total energy and momentum
    total_energy = 0.0
    total_momentum = np.array([0.0, 0.0, 0.0])

    for particle in bodies:
        # print(particle.name, particle.mass, particle.position, particle.velocity, particle.acceleration)
        particle.updateGravaccel(bodies)

        if method == 1:
            particle.updateE(deltaT)
        elif method == 2:
            particle.updateEC(deltaT)
        elif method ==3:
            particle.updateVerlet(bodies, deltaT)
        
        xpos[particle.name].append(particle.position[0])
        ypos[particle.name].append(particle.position[1])
        zpos[particle.name].append(particle.position[2])
        
        
    time += deltaT
    
    
    linear_momentum = sum(particle.linearMomentum() for particle in bodies)
    linearMom.append(np.linalg.norm(linear_momentum))
# 
    angularMomentum = np.sum([np.float64(particle.angularMomentum()) for particle in bodies], axis=0)
    angularMom.append(np.float64(np.linalg.norm(angularMomentum)))

    for p in bodies:
        total_energy += np.float64(p.kineticEnergy() + 0.5 * p.potentialEnergy(bodies))
    totalEnergy.append(np.float64(total_energy))
    



orbits2D()
orbits3D()
EnergyCons()
LinearMomCons()
AngMomCons()

linearMom.sort()
print(linearMom[0], linearMom[-1])
totalEnergy.sort()
print(totalEnergy[0],totalEnergy[1])
angularMom.sort()
print(angularMom[0], angularMom[1])
with open(r"final project\output.txt", "w") as f:  
    f.writelines(linearMom)
with open(r"final project\output2.txt", "w") as g:
    g.writelines(timeLog)

f.close()
g.close()

"""
# 1.170935903e+17
# 7.3360039e+23

# Px has variation +7e23 decr.
# Py has variation +3e23 inc.
# Pz has variation +1.2e23 inc. (e29)
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



list to do:
linear momentum - CONVSERED
kepler
verlet
graphs
user input
"""

