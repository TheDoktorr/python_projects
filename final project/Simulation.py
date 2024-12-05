import numpy as np
from Setup import *
from Graphs import *


time = 0
progress = 0
no_planets = len(bodies)
print(planets)

deltaT = 3600
method = 2
iterations = int(31_557_600 / deltaT)
years = 1


print(f"running the simulation for {no_planets} bodies, {years} years, with a time step of {deltaT} seconds. ")
print(f"(This will run for {iterations} iterations)")
if method == 1:
    print("You have chosen the Euler (forward) Method!")
elif method == 2:
    print("You have chosen the Euler-Cromer Method!")
elif method ==3:
    print("You have chosen the Verlet Method!")





# main simulation loop

for i in range(iterations):

    timeLog.append(time)
    
   
    total_momentum = np.array([0.0, 0.0, 0.0])

    for particle in bodies:       
        particle.updateGravaccel(bodies)

    for particle in bodies:

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

    kinetic_energy = 0.0
    potential_energy = 0.0
    total_energy = np.float64(0.0)
    for p in bodies:
        total_energy += np.float64(p.kineticEnergy() + 0.5 * p.potentialEnergy(bodies))
    totalEnergy.append(np.float64(total_energy))
    """
    kinetic_energy = sum(body.kineticEnergy() for body in bodies)
    potential_energy = sum(0.5 * body.potentialEnergy(bodies) for body in bodies)
    total_energy = kinetic_energy + potential_energy
    totalEnergy.append(np.float64(total_energy))
   
    for k, p1 in enumerate(bodies):
        kinetic_energy += p1.kineticEnergy()  # Kinetic energy for each particle
        for j, p2 in enumerate(bodies):
            if j > k:  # Only calculate potential energy once per pair
                distance = np.linalg.norm(p1.position - p2.position)
                potential_energy += (-p1.G * p1.mass * p2.mass) / (distance)

    total_energy = kinetic_energy + potential_energy
    totalEnergy.append(total_energy)
    """
    tenpercent = (iterations) / 10 
    
    if i % tenpercent < 1:
        print(f"{progress}%")
        progress += 10
    if i % 10000 == 0:
        timeLogS.append(time)
        totalEnergyS.append(np.float64(total_energy))
        linearMomS.append(np.linalg.norm(linear_momentum))
        angularMomS.append(np.float64(np.linalg.norm(angularMomentum)))

    
print("The simulation has finished")
with open(r'final project/output.txt', 'w') as f:
    for j in range(len(timeLogS)):
        f.write(f" time {timeLogS[j]} \n system total energy {totalEnergyS[j]} \n total linear momentum {linearMomS[j]} \n and total angular momentum {angularMomS[j]}\n")
    print("\n", file = f)
    linearMom.sort()
    print(f"Minimum linear momentum: {linearMom[0]} \n Maximum linear momentum: {linearMom[-1]} \n", file = f )
    print("\n", file = f)
    totalEnergy.sort()
    print(f"Minimum total Energy: {totalEnergy[0]} \n Maximum total Energy: {totalEnergy[-1]} \n", file = f )
    print("\n", file = f)
    angularMom.sort()
    print(f"Minimum angular momentum: {angularMom[0]} \n Maximum angular momentum: {angularMom[-1]} \n", file = f )


orbits2D()
orbits3D()
EnergyCons()
LinearMomCons()
AngMomCons()





"""
with open(r"final project/output.txt", "w") as f:  
    f.writelines(linearMom)
with open(r"final project/output2.txt", "w") as g:
    g.writelines(timeLog)

f.close()
g.close()


# 1.170935903e+17
# 7.3360039e+23

# Px has variation +7e23 decr.
# Py has variation +3e23 inc.
# Pz has variation +1.2e23 inc. (e29)
linearMom = np.array(linearMom)


list to do:

kepler
angular kinetic 
graphs
user input
"""

