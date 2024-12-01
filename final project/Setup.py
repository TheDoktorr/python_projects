import numpy as np
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from astropy.constants import G
from spiceypy import sxform, mxvg
from poliastro import constants

from Particle import Particle

 # Using Astropy, we import the time
t = Time("2024-11-26 17:00:00.0", scale="tdb")

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


# dictionary reference of mass constants for ClassMaker to reference
GM_constants = {
    "sun": constants.GM_sun,
    "mercury": constants.GM_mercury,
    "venus": constants.GM_venus,
    "earth": constants.GM_earth,
    "mars": constants.GM_mars,
    "jupiter": constants.GM_jupiter,
    "saturn": constants.GM_saturn,
    "uranus": constants.GM_uranus,
    "neptune": constants.GM_neptune


}


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


    body = Particle(position=np.array(coord_conv(body_input_l)[0]),     # coord_conv outputs (new_position, new_velocity)
                    velocity=np.array(coord_conv(body_input_l)[1]),     # index ensures the correct element is chosen
                    acceleration=np.array([0, 0, 0]),                   # accel initialised to 0, later updated
                    name=body_input_U,                                  # var names capitalised
                    mass = massFunc(body_input_l) )                     

    return body



# planets = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets = ["Sun", "Mercury", "Venus", "Earth"]
# planets = ["Sun", "Earth"]
bodies = []


for i in range(len(planets)):       # for each planet
    
    body = ClassMaker(planets[i])   # make a class associated with it
    bodies.append(body)             # add to list
    
# setup body coordinate lists, as blank lists
xpos = {particle.name: [] for particle in bodies}   
ypos = {particle.name: [] for particle in bodies}
zpos = {particle.name: [] for particle in bodies}


#time and energy for logging and graphing
timeLog = []
linearMom = []
angularMom =[]
totalEnergy = []


