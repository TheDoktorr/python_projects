from poliastro import constants
from astropy.time import Time

 # Using Astropy, we import the time
t = Time("2024-11-26 17:00:00.0", scale="tdb")

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
    "neptune": constants.GM_neptune, 
    "pluto": constants.GM_pluto, 
    "moon": constants.GM_moon,
    "phobos": constants.GM_phobos,
    "deimos": constants.GM_deimos,
    "europa": constants.GM_europa,
    "ganymede": constants.GM_ganymede,
    "enceladus": constants.GM_enceladus,
    "titan": constants.GM_titan,
    "titania": constants.GM_titania,
    "triton": constants.GM_triton,
    "charon": constants.GM_charon
}

