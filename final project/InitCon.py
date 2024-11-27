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
sun_pos, sun_vel = get_body_barycentric_posvel("sun", t, ephemeris="jpl")
pos, vel = get_body_barycentric_posvel("earth", t, ephemeris="jpl")
"""
pos, vel = get_body_barycentric_posvel("mercury", t, ephemeris="jpl")
pos, vel = get_body_barycentric_posvel("venus", t, ephemeris="jpl")
pos, vel = get_body_barycentric_posvel("earth-moon-barycenter", t, ephemeris="jpl")
pos, vel = get_body_barycentric_posvel("mars", t, ephemeris="jpl")
pos, vel = get_body_barycentric_posvel("jupiter", t, ephemeris="jpl")
pos, vel = get_body_barycentric_posvel("saturn", t, ephemeris="jpl")
pos, vel = get_body_barycentric_posvel("uranus", t, ephemeris="jpl")
pos, vel = get_body_barycentric_posvel("neptune", t, ephemeris="jpl")
"""

# convert to ecliptic coordinate frame, method in notes

# for the sun:
sun_statevec = [
    sun_pos.xyz[0].to("m").value,
    sun_pos.xyz[1].to("m").value,
    sun_pos.xyz[2].to("m").value,
    sun_vel.xyz[0].to("m/s").value,
    sun_vel.xyz[1].to("m/s").value,
    sun_vel.xyz[2].to("m/s").value,
]

# get transformation matrix to the ecliptic (use time in Julian Days)
sun_trans = sxform("J2000", "ECLIPJ2000", t.jd)

# transform state vector to ecliptic
sun_statevececl = mxvg(sun_trans, sun_statevec)

# get positions and velocities
sun_pos1 = [sun_statevececl[0], sun_statevececl[1], sun_statevececl[2]]
sun_vel1 = [sun_statevececl[3], sun_statevececl[4], sun_statevececl[5]]

# sun mass (in kg)
sun_m = (constants.GM_sun / G).value






# and for earth
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
position = [statevececl[0], statevececl[1], statevececl[2]]
velocity = [statevececl[3], statevececl[4], statevececl[5]]

# earth mass
earth_m = (constants.GM_earth / G).value



# sun particle instance
sun = Particle(
    position=np.array(sun_pos1),
    velocity=np.array(sun_vel1),
    acceleration=np.array([0, 0, 0]),
    name="Sun",
    mass = sun_m
)
earth = Particle(
    position=np.array(position),
    velocity=np.array(velocity),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass = earth_m
)
