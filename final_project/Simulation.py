import numpy as np
from Setup import *
from Graphs import *

time = 0
progress = 0
no_planets = len(bodies)


clear_terminal()
print(planets)
print(f"running the simulation for {no_planets} bodies, {years} years, with a time step of {deltaT} seconds. ")
print(f"(This will run for {iterations} iterations)")
if method == 1:
    print("You have chosen the Euler (forward) Method!\n")
elif method == 2:
    print("You have chosen the Euler-Cromer Method!\n")
elif method ==3:
    print("You have chosen the Verlet Method!\n")


rerun = input("Do you want to re-run the simulation ? (y/n):\n"
              "(note if this is first run no data will be cached)\n").strip().lower()
# main simulation loop
if rerun == "y":
    for i in range(iterations):

        timeLog.append(time)
        
        total_momentum = np.array([0.0, 0.0, 0.0])

        for particle in bodies:       
            particle.updateGravaccel(bodies)

        if method == 3:
            particle.updateVerlet(bodies, deltaT)
        for particle in bodies:

            if method == 1:
                particle.updateE(deltaT)
            elif method == 2:
                particle.updateEC(deltaT)
        #  elif method ==3:
        #     particle.updateVerlet(bodies, deltaT)
            
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
        kinetic_energy = sum(body.kineticEnergy() for body in bodies)
        kineticEnergy.append(kinetic_energy)

        potential_energy = sum(0.5 * body.potentialEnergy(bodies) for body in bodies)
        potentialEnergy.append(potential_energy)
        for p in bodies:
            total_energy += np.float64(p.kineticEnergy() + 0.5 * p.potentialEnergy(bodies))
        totalEnergy.append(np.float64(total_energy))

        tenpercent = (iterations) / 10 
        
        if i % tenpercent < 1:
            print(f"{progress}%")
            progress += 10
        if i % 1000 == 0:
            timeLogS.append(time)
            totalEnergyS.append(np.float64(total_energy))
            linearMomS.append(np.linalg.norm(linear_momentum))
            angularMomS.append(np.float64(np.linalg.norm(angularMomentum)))
    print("The simulation has finished")

elif rerun == "n":
    print("Using cached data if available")
else:
    print("Invalid input! Please enter 'y' or 'n'.")

    
graphs = input("would you like to produce graphs relating to the simulation data? (y/n):\n").strip().lower()
if graphs == "y":
    orbits2D()
    orbits3D()
    EnergyCons()
    EnergyCons2()
    EnergyKinetic()
    EnergyPotential()
    LinearMomCons()
    AngMomCons()
elif graphs == "n":
    print("no graphs will be printed")
else:
    print("Invalid input! Please enter 'y' or 'n'.")



# aphelion_perihelion(xpos, ypos, zpos)
Kepler_three()


with open(r'final project/output.txt', 'w') as f:
    for j in range(len(timeLogS)):
        f.write(f" time {timeLogS[j]} \n system total energy {totalEnergyS[j]} \n total linear momentum {linearMomS[j]} \n and total angular momentum {angularMomS[j]}\n \n")
    print("\n", file = f)
    print("system totals", file = f)
    linearMom.sort()
    print(f"Minimum linear momentum: {linearMom[0]} \n Maximum linear momentum: {linearMom[-1]} \n", file = f )
    print("\n", file = f)
    totalEnergy.sort()
    print(f"Minimum total Energy: {totalEnergy[0]} \n Maximum total Energy: {totalEnergy[-1]} \n", file = f )
    print("\n", file = f)
    angularMom.sort()
    print(f"Minimum angular momentum: {angularMom[0]} \n Maximum angular momentum: {angularMom[-1]} \n", file = f )


 # body crosses from -y to +y





"""

# 1.170935903e+17
# 7.3360039e+23

# Px has variation +7e23 decr.
# Py has variation +3e23 inc.
# Pz has variation +1.2e23 inc. (e29)
linearMom = np.array(linearMom)


list to do:

angular kinetic  x
graphs
user input
"""

