class SimpsonIntegration:
    """
    Class to setup an integration instance with an associated function.

    Parameters
    ----------
    function: callable
        The function to be integrated.
    eps: float
        A value defining the absolute target precision of the integration.
    """

    def __init__(self, function, eps=1e-3):
        self.setFunction(function)
        self.setEPS(eps)

    def setFunction(self, function):
        if not callable(function):
            raise TypeError("You have not supplied a valid function")
        self.functionToBeIntegrated = function
        
    def setEPS(self, eps):
        if eps <= 0:
            raise ValueError("Precision must be a positive number")
        self.eps = eps

    def evaluate(self, a, b):
        """
        Performs the integration using the Simpson method

        Parameters
        ----------
        self:
            Since this is a method (a function inside a class)
            this is required
        a: float
            Lower bound of the integral
        b: float
            Upper bound of the integral
        """

        #In order to perform the integration, we need to set an initial
        # number of intervals to perform the 
        N = 10

        #Setup some variables that we can use to keep track of the
        # integral convergence, and therefore when we have reached
        # the target precision

        #Here we store the previous result of the integral evaluation.
        previous = 0
        #Here we store the absolute difference between the current and previous
        # integral evaluations
        err = 1e5

        #This while loop runs until err reaches (falls below) the target precision (self.eps)
        while err > self.eps:
            #Evalute the integral with the current N
            # All other function arguments remain fixed for the lifetime of the while loop
            current = self.simpson(a, b, N, self.functionToBeIntegrated)
            #Evaluate the absolute difference between current & previous
            # This is a measure of the convergence
            # We do not know a priori what the answer is
            err = abs(current - previous)
            #Increase the value of N for the next iteration of the while loop
            N = 2 * N
            #Store the current value as the previous, 
            # such that it's available for the next iteration of the while loop
            previous = current

        #Finally we return the current value of the integral,
        # as it is when the while loop ends
        # This is the value of the integral to the target precision
        return current

    @staticmethod
    def simpson(a, b, N, f):

        """
        Simpson rule for numerical integration of a function.

        Parameters:
        -----------
        a: float
            Lower bound of the integral
        b: float
            Upper bound of the integral (must be >a)
        N: int
            Number of intervals (must be an even number)
        f: callable
            Function to be integrated
        """

        # We first check whether the arguments are valid
        # If not, a ValueError is raised

        if a >= b:
            raise ValueError(
                "The lower bound is greater than or equal to the upper bound"
            )
        
        if not isinstance(N, int):
            raise TypeError(
                "The number of intervals must be an integer"
            )

        if (N%2 != 0):
            raise ValueError(
                "The Simpson's rule requires an even number of intervals"
            )
        
        #We then implement the Simpson's rule equation, as found in the course notes at
        # https://www.lancaster.ac.uk/staff/drummonn/PHYS281/numerical-integration/
        # (final equation)
        
        dx = (b - a) / N

        integral_lr = 0

        for i in range(1,N):

            xi = a + i * dx

            if (i%2 == 1):
                integral += 4*f(xi)
            else:
                integral += 2*f(xi)

        integral += f(a) + f(b)
        integral = dx/3 * integral

        return integral






   
