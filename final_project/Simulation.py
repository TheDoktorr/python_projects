import numpy as np
from Setup import *
import matplotlib.pyplot as plt

time = 0
progress = 0
no_planets = len(bodies)

def orbits2D():
    fig=plt.figure(figsize=(3.5,2.6),dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$x$ (au)')
    ax.set_ylabel(r'$y$ (au)')
    for name in xpos:
        x = np.array(xpos[name]) /149597870700  # from NASA
        y= np.array(ypos[name]) /149597870700
        ax.plot(x, y, label = name, lw=0.4)
    ax.legend()
   # plt.savefig("2DorbitsV2.svg")
    plt.show()

def EnergyCons():
    fig=plt.figure(figsize=(3.5,2.6),dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$E$ (J)')
    ax.plot(timeLog, totalEnergy, label="Total Energy", lw=0.4)
    ax.legend()
   # plt.savefig("EnergyConsV2.svg")
    plt.show()

def EnergyCons2():
    fig=plt.figure(figsize=(3.5,2.6),dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$E$ (J)')
    ax.plot(timeLog, kineticEnergy, label="Kinetic E", lw=0.4)
    ax.plot(timeLog, potentialEnergy, label="Potential E", lw=0.4)
    ax.legend()
  #  plt.savefig("EnergyCons2V2.svg")
    plt.show()

def LinearMomCons():
    fig=plt.figure(dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$ (kg m/s$')
   # linearMom = np.array(linearMom)
    ax.plot(timeLog, linearMom, label="Linear Momentum", lw=1)
    ax.legend()
  #  plt.savefig("LinMomentumV2.svg")
    plt.show()

def AngMomCons():
    fig=plt.figure(dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$kg m/s^2$ (J)')
    ax.plot(timeLog, angularMom, label="Angular Momentum", lw=0.4)
    ax.legend()
  #  plt.savefig("AngMomentumV2.svg")
    plt.show()
 
def orbits3D():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    for name in xpos:
        # change units to astronomical units
        xx = np.array(xpos[name]) /149597870700
        yy= np.array(ypos[name]) /149597870700
        zz = np.array(zpos[name]) /149597870700
        ax.plot(xx, yy, zz, label = name, lw=0.4) 
    ax.set_xlabel(r'$x$ (au)')
    ax.set_ylabel(r'$y$ (au)')
    ax.set_zlabel(r'$z$ (au)')
    ax.legend()
    plt.show()

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
              "(note if this is first run no data will be cached - cache is based on last run ONLY)\n").strip().lower()
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
    print("Storing data please wait....")
    data_store = {
        "timeLog" : timeLog,
        "linearMom" : linearMom,
        "angularMom" : angularMom, 
        "totalEnergy" : totalEnergy,
        "kineticEnergy": kineticEnergy,
        "potentialEnergy" : potentialEnergy,
        "xpos" : xpos,
        "ypos" : ypos,
        "zpos" : zpos  }
    save_pickle(data_store)
    
    print("Kepler's law orbits:\n")
    orbit_list = Kepler_three()
    for j in range(len(orbit_list)):
        print(orbit_list[j])

elif rerun == "n":
    print("Using cached data (from last full run) if available")
    loaded_data = load_pickle()
    timeLog = loaded_data["timeLog"]
    linearMom = loaded_data["linearMom"]
    angularMom =loaded_data["angularMom"]
    totalEnergy = loaded_data["totalEnergy"]
    kineticEnergy = loaded_data["kineticEnergy"]
    potentialEnergy = loaded_data["potentialEnergy"]
    xpos = loaded_data["xpos"]
    ypos = loaded_data["ypos"]
    zpos = loaded_data["zpos"]

else:
    print("Invalid input! Please enter 'y' or 'n'.")
    
graphs = input("would you like to produce graphs relating to the simulation data? (y/n):\n").strip().lower()
if graphs == "y":
    orbits2D()
    orbits3D()
    EnergyCons()
    EnergyCons2()
    LinearMomCons()
    AngMomCons()
elif graphs == "n":
    print("no graphs will be printed")
else:
    print("Invalid input! Please enter 'y' or 'n'.")


with open(r'final_project\output.txt', 'w') as f:
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


"""

list to do:
tidy up
user body input
"""

