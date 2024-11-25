import numpy as np

class Particle:
    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, -10, 0], dtype=float),
        name='Ball',
        mass=1.0,
        G = 6.67408E-11
    ):
        self.position = np.copy(position).astype(float)
        self.velocity = np.copy(velocity).astype(float)
        self.acceleration = np.copy(acceleration).astype(float)
        self.name = np.copy(name)
        self.mass = np.copy(mass)
        self.G = G
        
        
    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
        self.name, self.mass,self.position, self.velocity, self.acceleration
    )

    def update(self, deltaT):
        self.deltaT = deltaT
        
        # define start variables 
        self.position = self.position + self.velocity * self.deltaT
        self.velocity = self.velocity  + self.acceleration * self.deltaT
        # if first particle =x second particle 
        return self.position, self.velocity
    
    def updateGravitationalAcceleration(self, body):
        # define Gravitational constant
  
        gravaccel = - (self.G * body.mass) * (body.position - self.position) / (np.linalg.norm(body.position - self.position ))**3
        return gravaccel
    


