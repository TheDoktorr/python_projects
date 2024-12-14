import numpy as np
from astropy.constants import G
import copy
"""
Particle class, used to model each planet as a body with attributes of position, velocity, acceleration, name and mass
"""
class Particle:
    # initialise the class with default parameters
    def __init__(   
        self,
        position=np.array([0, 0, 0], dtype=np.float64),     # arrays used to make maths easier with numpy
        velocity=np.array([0, 0, 0], dtype=np.float64),
        acceleration=np.array([0, -10, 0], dtype=np.float64),
        name="point particle",
        mass=1.0,
        G = G
    ):
        self.position = np.array(np.copy(position), dtype=np.float64)   # copy class attributes so initial conditions are unchanged when initialised
        self.velocity = np.array(np.copy(velocity), dtype=np.float64)
        self.acceleration = np.array(np.copy(acceleration), dtype=np.float64)
        self.name = name
        self.mass = np.float64(mass)
        self.G = np.float64(G)
        
    def __str__(self): # string input is initialised 
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

    def updateEC(self, deltaT):
        """
        Alternative method for updating based on Euler-Cromer method 
        takes self. position, velocity,, acceleration and time-step deltaT 
        """
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT



    def updateGravaccel(self, bodies):
        """
        Method for many body acceleration of bodies, based on newtons gravitational law
        list of bodies, e.g [satellite1, satellite2]
        """
        total_gravaccel = np.array([0.0, 0.0, 0.0])          # initialise to 0 array 
        for body in bodies:
            if body is not self:                                          # avoid calculating acceleration with respect to itself
                distance = np.linalg.norm(self.position - body.position)     # calculate distance between bodies
   
                epsilon = 1e-6  # Softening factor
                if distance < 1e-25:
                    distance = np.sqrt(distance**2 + epsilon**2)  # Softened distance for very small distances to avoid "exploding" acceleration

                gravaccel = -np.float64(self.G * body.mass) * (self.position - body.position) / (distance**3)           # acceleration calculated 
                total_gravaccel += np.array(gravaccel, dtype=np.float64)                                                                #  add each gravaccel calculation to the total 

        self.acceleration = np.array(total_gravaccel, dtype=np.float64)                                                                # assign the gravaccel to be the particle acceleration
        
    def updateVerlet(self, bodies, deltaT):
        """
        Method for approximating positions and velocities based on accelerations, using end accelerations to update velocity
        This smooths out changes in acceleration
        input also requires bodies to update end acceleration
        bodies are saved to a state after each operation, using copies - this is likely not the best way of doing this!

        """    
        i =0                                                                                                                                                              # set initialisation to 0
        estimatedbodies = [np.zeros(3, dtype=np.float64) for j in range(len(bodies))]                                          # initialises the estimated bodies list to be 0 for the length of the input list
        for body in bodies:
            body.position = body.position + body.velocity*deltaT + 0.5*body.acceleration*(deltaT)**2                # update position of each body 
            estimatedbodies[i] = copy.deepcopy(body)                                                                                           # deepcopy the updated bodies to each element of the estimated bodies list
            i += 1                                                                                                                                                      # incriment loop, so each body is updated then copied to our estimated list

        bodiescopy = copy.deepcopy(estimatedbodies)                                                                                        # copy the list of estimated bodies 
        i = 0   
        for body in bodies:                             
            estimatedbodies[i].updateGravaccel(bodiescopy)                                                                                  # for each body, update acceleration with respect to a fixed copy of the list, bodiescopy
            i += 1                                                                                                                                                      # incriment the loop, so each body is updated and reassigned to the esimated list
                                                                                                                                                                            # this method ensures each list is "preserved" after each step
        i=0
        for body in bodies:                                                                                                                         
            body.velocity = body.velocity + 0.5*(estimatedbodies[i].acceleration + body.acceleration)*deltaT     # same process, using estimated bodies acceleration as our endpoint acceleration to update body velocity
            i += 1

    def kineticEnergy(self):    
        """
        Takes body input, uses velocity and mass to calculate kinetic energy of the body 
        """
        Kvelocity= np.linalg.norm(self.velocity)        # take the norm of the velocity 

        Kenergy =  0.5 * self.mass * Kvelocity**2

        return Kenergy

    def potentialEnergy(self, bodies):          
        """
        Calculates potential energy of the body with respect to each other body
        requires body and self inputs for mass and distance relative to other bodies
        """
        potentialE = 0              # intialised quantity to 0
        epsilon = 1e-5             # softening factor to avoid "explosion" when dividing by small distances
        for body in bodies:
            if body is not self:    # avoid potential with respect to itself
                distance = np.linalg.norm(self.position - body.position)            # distance between bodies calculated
                U = ( -self.G * self.mass * body.mass ) / (distance+epsilon)       # potential with respect to other bodies calculated by standard results
                potentialE += U                                                                          # each contribution added to total value
        return potentialE
    
    def linearMomentum(self):                           
        """
        Function to return linear momentum using mass and velocity
        """
        return self.mass * self.velocity
    
    def angularMomentum(self):
        """
        Function that uses position mass and velocity to return angular momentum of each body using L = r x p
        """
        return np.cross(self.position, (self.mass * self.velocity))


