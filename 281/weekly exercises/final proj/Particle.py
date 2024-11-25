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

    def updateE(self, deltaT):
        """
        Update position and velocity based on the Euler Method
        takes self.position, velocity, acceleration as passed to it
        takes deltaT as the time step of the update
        """

        self.deltaT = deltaT
        
        self.position = self.position + self.velocity * self.deltaT
        self.velocity = self.velocity  + self.acceleration * self.deltaT

        return self.position, self.velocity
    
    def updateEC(self, deltaT):
        """
        Alternative method for updating based on Euler-Cromer method 
        
        """
        self.deltaT = deltaT 
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT

        return self.position, self.velocity

    def updateER(self, deltaT):
        """
        Place holder for Euler-richardson        
        """

    def updateGravitationalAcceleration(self, body):
        
        # handle divide by 0 errors:
        distance = np.linalg.norm(self.position - body.position)
        if distance == 0:
            return np.array([0.0, 0.0, 0.0])
       

        gravaccel = - (self.G * body.mass) * (self.position - body.position) / (distance ** 3)
        self.acceleration = gravaccel
        return gravaccel
    
    def updateGravAccel(self, bodies):
        

        return gravaccel

    def kineticEnergy(self):
        Kvelocity= np.linalg.norm(self.velocity)

        Kenergy =  0.5 * self.mass * Kvelocity**2

        return Kenergy
    
