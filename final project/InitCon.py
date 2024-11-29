import numpy as np
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from astropy.constants import G
from spiceypy import sxform, mxvg
from poliastro import constants


from Particle import Particle


"""
earthMass = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass
)

satPosition = earthRadius + (35786 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite = Particle(
    position=np.array([satPosition, 0, 0]),
    velocity=np.array([0, satVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=100.
)

satPosition = earthRadius + (35992 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite2 = Particle(
    position=np.array([satPosition, 0, 0]),
    velocity=np.array([0, satVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=150.
)
"""
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


# earth mass
# Earth_m = (constants.GM_earth / G).value
# sun mass (in kg)
# Sun_m = (constants.GM_sun / G).value

def UpperCase(lower):
    lowertxt = str(lower)
    lowertxt = lowertxt.capitalize()
    return lowertxt
    
def LowerCase(Upper):
    Uppertxt = str(Upper)
    Uppertxt = Uppertxt.lower()
    return Uppertxt



GM_constants = {
    "sun": constants.GM_sun,
    "earth": constants.GM_earth,
    "mercury": constants.GM_mercury,
    "venus": constants.GM_venus,
    "mars": constants.GM_mars,
    "jupiter": constants.GM_jupiter,
    "saturn": constants.GM_saturn,
    "uranus": constants.GM_uranus,
    "neptune": constants.GM_neptune


}

def massFunc(body_input):
    # dynamically building the variable   
    if body_input in GM_constants:
        GM_input = GM_constants[body_input]
        return (GM_input / G).value
    else:
        raise ValueError("No mass found for that body")


def ClassMaker(body_input):
    body_input_l = LowerCase(body_input) 
    body_input_U =UpperCase(body_input)

    body = Particle(position=np.array(coord_conv(body_input_l)[0]), 
                    velocity=np.array(coord_conv(body_input_l)[1]), 
                    acceleration=np.array([0, 0, 0]),  
                    name=body_input_U,    
                    mass = massFunc(body_input_l) )

    return body



