import numpy as np
from astropy.coordinates import get_body_barycentric_posvel
from astropy.constants import G
from spiceypy import sxform, mxvg
import os
import platform

from Particle import Particle
from Constants import *


# we now get the positions and velocities of solar system bodies
def coord_conv(body):
    # convert input into string to obtain data
    body =str(body)
    pos, vel = get_body_barycentric_posvel(body, t, ephemeris="jpl")      # check this works

    # make a "state vector" of positions and velocities (in metres and metres/second, respectively)
    statevec = [
        pos.xyz[0].to("m").value,
        pos.xyz[1].to("m").value,
        pos.xyz[2].to("m").value,
        vel.xyz[0].to("m/s").value,
        vel.xyz[1].to("m/s").value,
        vel.xyz[2].to("m/s").value,
        ]

    # get transformation matrix to the ecliptic (use time in Julian Days)
    trans = sxform("J2000", "ECLIPJ2000", t.jd)

    # transform state vector to ecliptic
    statevececl = mxvg(trans, statevec)

    # get positions and velocities
    new_position = [statevececl[0], statevececl[1], statevececl[2]]
    new_velocity = [statevececl[3], statevececl[4], statevececl[5]]

    return new_position, new_velocity


# function to change input to uppercase, to work with variable names
def UpperCase(lower):
    lowertxt = str(lower)
    lowertxt = lowertxt.capitalize()
    return lowertxt

# function to make word lowercase, as JPL names are all lowercase    
def LowerCase(Upper):
    Uppertxt = str(Upper)
    Uppertxt = Uppertxt.lower()
    return Uppertxt

def massFunc(body_input):
    """
    This function uses the dictionary GM_constants to point to the correct mass based on the input
    Output: mass in kilograms
    """
    # dynamically assign the variable 
    if body_input in GM_constants:
        GM_input = GM_constants[body_input]
        return (GM_input / G).value                         # ensure /G to keep units in kg
    else:
        raise ValueError("No mass found for that body")     # error if body is not found in the dictionary


def ClassMaker(body_input):
    """
    This function takes the body input single value and generates the initial conditions based on the JPL library
    """
    # this means regardless of input JPL can find the right values, and value names are capitalised
    body_input_l = LowerCase(body_input) 
    body_input_U = UpperCase(body_input)


    body = Particle(position=np.array(coord_conv(body_input_l)[0], dtype=np.float64),      # coord_conv outputs (new_position, new_velocity)
                    velocity=np.array(coord_conv(body_input_l)[1], dtype=np.float64),                 # index ensures the correct element is chosen
                    acceleration=np.array([0, 0, 0], dtype=np.float64),                                           # accel initialised to 0, later updated
                    name=body_input_U,                                                                                        # var names capitalised
                    mass = massFunc(body_input_l) )                     

    return body

planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

def update_planets(new_list):
    global planets
    planets[:] = new_list

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # Clear screen on Windows
    else:
        os.system("clear")  # Clear screen on Linux/Mac

# user input system


while True:
    # Single input for y/n
    print("Simulatoin setup!")
    user_input = input("Would you like to use a preset system? (y / n): ").strip().lower()
    
    if user_input == "y":
        # Provide preset options
        print("2 body (Sun and Earth) for 1 Julian year, time-step 1 minute (1)\n"
            "4 body (Sun to Earth) for 1 Julian year, time-step 1 hour  (2) \n"
              "9 body (Sun to Neptune) for 170 years, time-step 1 day (3) \n")
    
        # Handle preset selection
        try:
            preset = int(input("Enter your preset choice (1 or 2): ").strip())
            
            if preset ==1:
                update_planets(["Sun", "Earth"])
                deltaT = 60
                iterations = int(31557600 / deltaT)
                years = 1

            elif preset == 2:
                update_planets(["Sun", "Mercury", "Venus", "Earth"])
                deltaT = 3600
                iterations = int(31557600 / deltaT)
                years = 1
                
            elif preset == 3:
                update_planets(["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
                deltaT = 86400
                iterations = int(170 * 31557600 / deltaT)
                years = 170

            else:
                raise ValueError("Invalid preset option selected.")
            
            # Ask for method choice
            method = int(input("What Method would you like to use, Euler (1), Euler-Cromer (2), or Verlet (3)? ").strip())
            if method not in [1, 2, 3]:
                raise ValueError("This is not one of the options!")
            break  # Exit the loop after successful input

        except ValueError as e:
            print(f"Error: {e}. Please try again.")
    
    elif user_input == "n":
        print("You can decide your own variables")
        print("Enter your desired planets in the form body1 body2 body3 \n"
              "please dont put any commas or separators in!")
        planets = input().split()
        print("please enter the timestep")
        deltaT = int(input())
        print("please enter the time to run the simulation for in years")
        years = int(input())
        iterations = int(years * 31557600 / deltaT)
        method = int(input("What Method would you like to use, Euler (1), Euler-Cromer (2), or Verlet (3)? ").strip())
        if method not in [1, 2, 3]:
            raise ValueError("This is not one of the options!")
          # Exit the loop after successful input
        break

    else:
        print("Invalid input! Please enter 'y' or 'n'.")


bodies = []

for i in range(len(planets)):       # for each planet
    
    body = ClassMaker(planets[i])   # make a class associated with it
    bodies.append(body)                 # add to list
    
# setup body coordinate lists, as blank lists
xpos = {particle.name: [] for particle in bodies}   
ypos = {particle.name: [] for particle in bodies}
zpos = {particle.name: [] for particle in bodies}

def aphelion_perihelion(xpos, ypos, zpos):
    aphelion = {}
    perihelion = {}
     # iterative over every name and set of positions, as an array for easier maths
    for name in xpos.keys():
        x = np.array(xpos[name])
        y = np.array(ypos[name])
        z = np.array(zpos[name])
         # calculate 3D distances from origin
        length = np.sqrt(x**2 + y**2 + z**2)
        # using the max and min of each of these, we take these to be our aphelion and perihelion
        aphelion[name] = np.max(length)
        perihelion[name] = np.min(length)

    return aphelion, perihelion

def Kepler_three():
    # keplers 3rd law, requires setup of xpos, ypos, zpos data to calculate the semi-major axis
    aphelion, perihelion = aphelion_perihelion(xpos, ypos, zpos)
    semi_major_axes = {name: (aphelion[name] + perihelion[name]) / 2 for name in xpos.keys()}
    orbital_period = {}
    for name in xpos.keys():
        r = semi_major_axes[name]
        orbital_period[name] = 2* np.pi * np.sqrt((r ** 3) / (constants.GM_sun.value))
        orbital_period[name] = orbital_period[name] / (60 * 60 * 24)
    for name, period in orbital_period.items():
        print(f"Orbital period for {name}: {period:.2f} days")
    return orbital_period

#time and energy for graphing
timeLog = []
linearMom = [] 
angularMom =[]
totalEnergy = []
kineticEnergy = []
potentialEnergy = []
# shorter lists to print output to txt file
timeLogS = []
linearMomS = [] 
angularMomS =[]
totalEnergyS = []