import numpy as np
from astropy.constants import G

class Particle:
    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=np.float64),
        velocity=np.array([0, 0, 0], dtype=np.float64),
        acceleration=np.array([0, -10, 0], dtype=np.float64),
        name="point particle",
        mass=1.0,
        G = G
    ):
        self.position = np.array(np.copy(position), dtype=np.float64)
        self.velocity = np.array(np.copy(velocity), dtype=np.float64)
        self.acceleration = np.array(np.copy(acceleration), dtype=np.float64)
        self.name = name
        self.mass = np.float64(mass)
        self.G = np.float64(G)
        
        
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
        
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT

        return self.position, self.velocity



    def updateGravitationalAcceleration(self, body):
        
        # handle divide by 0 errors:
        distance = np.linalg.norm(self.position - body.position)
       # if distance == 0:
           # return np.array([0.0, 0.0, 0.0])
       
        while distance > 0:
            gravaccel = - (self.G * body.mass) * (self.position - body.position) / (distance ** 3)
            self.acceleration = gravaccel
        return gravaccel
    
    def updateGravaccel(self, bodies):
        """
        Method for many body acceleration of bodies 
        list of bodies, e.g [satellite1, satellite2]

        self = i
        bodies = j
        """
        total_gravaccel = np.array([0.0, 0.0, 0.0])
        for body in bodies:
            if body is not self:
               # epsilon = 1e-6
                distance = np.linalg.norm(self.position - body.position)
               # distance = np.sqrt(distance**2 + epsilon**2)
                
                epsilon = 1e-6  # Softening factor
                if distance < 1e-25:
                    distance = np.sqrt(distance**2 + epsilon**2)  # Softened distance

                gravaccel = -np.float64(self.G * body.mass) * (self.position - body.position) / (distance**3)
                total_gravaccel += np.array(gravaccel, dtype=np.float64)

        self.acceleration = np.array(total_gravaccel, dtype=np.float64)
        
    

    def kineticEnergy(self):
        Kvelocity= np.linalg.norm(self.velocity)

        Kenergy =  0.5 * self.mass * Kvelocity**2

        return Kenergy


    def potentialEnergy(self, bodies):
        potentialE = 0 
        for body in bodies:

            distance = np.linalg.norm(self.position - body.position)
            if body is not self:
                if distance < 1e-25:
                    distance += 1e-10

                U = ( -self.G * self.mass * body.mass ) / distance
                potentialE += U


        return potentialE
    
    def linearMomentum(self):
        clm = np.array([0, 0, 0], dtype=np.float64)
        
        linear_Momentum = self.mass * self.velocity
        clm += linear_Momentum
        return self.mass * self.velocity
    
    def angularMomentum(self):

        return np.cross(self.position, (self.mass * self.velocity))

    def masscaller(self):
        return self.mass
    
