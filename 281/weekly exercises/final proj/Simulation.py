import numpy as np
from Particle import Particle
import copy

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

iterations = 2000
time = 0 
deltaT = 6
Data = []

# original iteration loop for Euler method
for i in range(iterations):
        Satellite.updateGravitationalAcceleration(Earth)
        Earth.updateGravitationalAcceleration(Satellite)
        Satellite.updateE(deltaT)
        Earth.updateE(deltaT)
        time += deltaT

        if i % 100 == 0:
                Data.append([time, copy.deepcopy(Earth), copy.deepcopy(Satellite)])

# np.save(r"281\weekly exercises\final proj\TwoBodyTest.npy", Data, allow_pickle=True)       


print("The Earth and Satellite's locations after {0} seconds are (using Euler):".format((2000*6)))
for particle in [Earth, Satellite]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


# same loop applied to Euler-Cromer
for i in range(iterations):
        Satellite.updateGravitationalAcceleration(Earth)
        Earth.updateGravitationalAcceleration(Satellite)
        Satellite.updateEC(deltaT)
        Earth.updateEC(deltaT)
        time += deltaT

print("The Earth and Satellite's locations, after {0} seconds are *using Euler-Cromer:".format((2000*6)))
for particle in [Earth, Satellite]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!

