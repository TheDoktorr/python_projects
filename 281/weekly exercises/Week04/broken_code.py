import math


class Derivative:
    def __init__(self, func):
        """
        Class used to find the derivative of a function.

        Parameters
        ----------
        func: callable
            The function to find the derivative of.
        """

        # check that the function is callable (i.e., it is a function not a variable)
        if callable(func):
            self.func = func
        else:
            raise TypeError("Func must be a callable function")

    def diff(self, x0=0.0, delta=1e-5):

        """
        Calculate the derivative of the function by numerically working out its
        gradient.

        Parameters
        ----------
        x0: float
            The value at which to find the derivative of the function (default
            is 0).
        delta: float
            The step over which to calculate the gradient (default is 0.00001).
        
        Returns
        -------
        dfdx: float
            The derivative of the function.
        """
        self.x0 = x0
        self.delta = delta
        # the lower value of x at which to calculate the derivative
        xl = self.x0 - self.delta 

        # the upper value of x at which to calculate the derivative
        xh = self.x0 + self.delta 

        # the function evaluated at xl and xh
        fl = self.func(xl)
        fh = self.func(xh)

        # get df/dx
        dfdx = (fh - fl / 2 * delta)

        return dfdx


# create an instance of the Derivative class to differentiate the math.sin function
D = Derivative(math.sin)

# calculate the derivative at 10 points from 0 to pi/4
dsindx = []
dx = (math.pi / 4) / (10 - 1)

for i in range(10):
    x = dx * i
    dsindx.append(D.diff(x0=x))

# print out the final value of the derivatives
print("The derivative of Sine at {0:.4f} is {1:.4f}".format(x, dsindx[9]))