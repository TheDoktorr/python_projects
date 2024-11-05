import math


class Integration:
    """
    Class to setup an integration instance with an associated function.

    Parameters
    ----------
    function: callable
        The function to be integrated.
    method: int
        An integer defining the integration method to use: 1 is trapezium rule,
        2 is left rectangle rule, 3 is centre rectangle. Default it to use the
        trapezium rule.
    eps: float
        A value defining the absolute precision of the integration.
    """

    def __init__(self, function, method=1, eps=1e-5):
        self.setFunction(function)
        self.setEPS(eps)
        self.setMethod(method)

    def __repr__(self):
        return "I(method {}, function {}, eps {})".format(
            self.integrationMethod.__name__,
            self.functionToBeIntegrated.__name__,
            self.eps
        )

    def setFunction(self, function):
        if not callable(function):
            raise TypeError("You have not supplied a valid function")
        self.functionToBeIntegrated = function

    def setMethod(self, method):
        if method == 1:
            self.integrationMethod = self.trapz
        elif method == 2:
            self.integrationMethod = self.lrect
        elif method == 3:
            self.integrationMethod = self.crect
        else:
            raise ValueError(
                "Unrecognised integration method. Method must be 1 "
                "(trapezoid), 2 (left rectangle), or 3 (centre rectangle)."
            )

    def setEPS(self, eps):
        if eps <= 0:
            raise ValueError("Precision must be a positive number")
        self.eps = eps

    def evaluate(self, a, b):
        """
        Evaluate the integral between the ranges a and b.

        Parameters
        ----------
        a: (int, float)
            The lower bound of the integral.
        b: (int, float)
            The upper bound of the integral.

        Return
        ------
        float:
            The result of the integral.
        """
        N = 100
        
        err= self.eps * 100
        
        function = self.functionToBeIntegrated
        method = self.integrationMethod
        previous = self.integrationMethod(a,b, 1, function)
        #  instead of previous = 0
        
        if a >= b:
            raise ValueError(
                "The lower bound is greater than or equal to the upper bound"
            )

        while err > self.eps:
            result = method(a, b, N, function)
            err = abs(result - previous)
            N = 2 * N 
            previous = result

        
        return result

    @staticmethod
    def lrect(a, b, N, f):

        """
        Rectangle (lower) rule for numerical integration of a function.

        Parameters:
        -----------
        a: float
            Lower bound of the integral
        b: float
            Upper bound of the integral (must be >a)
        N: int
            Number of intervals
        f: callable
            Function to be integrated
        """
        if not isinstance(N, int):
            raise TypeError(
                "The number of intervals must be an integer"
            )
        
        h = (b - a) / N
        integral = 0

        for i in range(1, N+1):
            xi = a + h * (i - 1)

            integral += h *f(xi)
        
        return integral 


    @staticmethod
    def crect(a, b, N, f):
        """
        Rectangle (centre/mid) rule for numerical integration of a function.

        Parameters:
        -----------
        a: float
            Lower bound of the integral
        b: float
            Upper bound of the integral (must be >a)
        N: int
            Number of intervals
        f: callable
            Function to be integrated
        """
        if not isinstance(N, int):
            raise TypeError(
                "The number of intervals must be an integer"
            )
        
        h = (b - a) / N
        integral = 0

        for i in range(1, N+1):
            xi = a + h * (i - 0.5)

            integral += h * f(xi)
        
        return integral 

    @staticmethod
    def trapz(a, b, N, f):
        """
        Trapezium method of numerical integration.

        Parameters
        ----------
        a: (int, float)
            The lower bound of integral
        b: (int, float)
            The upper bound of integral
        N: int
            The number of intervals to use.
        f: callable
            The function to be integrated.
        """

        if not isinstance(N, int):
            raise TypeError(
                "The number of intervals must be an integer"
            )
        
        h = (b - a)/ N
    #  x1 = a
    # xn1 = b
        
        integral = 0 

        for i in range(2, N+1):
            xi =  a + h * (i - 1)
            integral += f(xi)


        integral += 0.5 * ( f(a) + f(b) )
        integral = h * integral 


        return integral
    

import math

def straight_line(x):
    m = 2.0  # gradient
    c = 2.0  # y-intercept
    return m * x + c

def quadratic(x):
    a = 2.2
    b = -3.5
    c = 6.7
    return a * x ** 2 + b * x + c

def test_function(x):
    return math.exp(-x) * x ** 5

def triangle(x):
    if x >= 0 and x <= 2:
        if x <= 1:
            return x
        else:
            return 2.0 - x
    else:
        return 0.0

functions = [straight_line, quadratic, test_function, triangle]
ranges = [[0.0, 1.0], [-10.0, 10.0], [1.0, 3.0], [-3.0, 4.0]]
analytical_answers = [3.0, 1600.6666666666666, 9.998850865646610741752695, 1.0]

wrong_precision = False
for i, func in enumerate(functions):
    myIntegral = Integration(func, method=2)
    for eps in [1e-1, 1e-2, 1e-3]:
        myIntegral.setEPS(eps)
        result = myIntegral.evaluate(ranges[i][0], ranges[i][1])
        if math.fabs(result - analytical_answers[i]) > eps:
            wrong_precision = True
            break
    if wrong_precision:
        break

if not wrong_precision:
    print("Integrals are evaluated to the correct precision using the left end-point rectangle rule")


