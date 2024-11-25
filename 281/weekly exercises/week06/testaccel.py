

import numpy as np 

class Body:
    def __init__(self, mass, position, G = 6.67408E-11): 
        self.mass = mass
        self.position = position
        self.G = G

    def updateGravitationalAcceleration(self, body):
        # Calculate the vector between the two bodies 
        r_vector = body.position - self.position
        # Calculate the magnitude of the vector 
        r_magnitude = np.linalg.norm(r_vector)
        # Calculate gravitational acceleration 
        grav_accel = - (self.G * body.mass) * r_vector / r_magnitude**3
        return grav_accel

# Example usage: 
body1 = Body(mass=5.972e24, position=np.array([0.0, 0.0, 0.0]))  # Earth, for instance 
body2 = Body(mass=7.348e22, position=np.array([384400000.0, 0.0, 0.0]))  # Moon, for instance 

# Calculating the gravitational acceleration on body1 due to body2
acceleration = body1.updateGravitationalAcceleration(body2)
print(acceleration)
