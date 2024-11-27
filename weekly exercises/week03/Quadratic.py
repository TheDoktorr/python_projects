"""
A skeleton template for the Quadratic class in Week 2: Coding Exercises.
"""

import math


class Quadratic:
    """ 
    A class representing a quadratic.

    It has three variables representing the coefficients of a quadratic of the
    form
    
    ax^2 + bx + c,
    
    where a, b and c are real constants.

    The so-called discriminant is b^2 - 4ac.

    If b^2 - 4ac < 0 the solutions are complex and will not be calculated.
    If b^2 - 4ac = 0 then there is one real root give by -b/(2a).
    If b^2 - 4ac > 0 then there are two real solutions.

    Parameters
    ----------
    a: (int, float)
        The coefficient of the x^2 term.
    b: (int, float)
        The coefficient of the x term.
    c: (int, float)
        The constant term (i.e., the coefficient of  the x^0 = 1 term).
    """

    def __init__(self, a, b, c):
        # The checks below make sure the coefficients are real numbers.
        if not isinstance(a, (int, float)):
            raise ValueError('Coefficient a is not a number')
        if not isinstance(b, (int, float)):
            raise ValueError('Coefficient b is not a number')
        if not isinstance(c, (int, float)):
            raise ValueError('Coefficient c is not a number')

        self.a = a
        self.b = b
        self.c = c

    def __str__( self ):
        return f"Q(x) = {self.a} x^2 + {self.b} x + {self.c}"

    def discriminant(self):
        disc = self.b**2 - (4* self.a * self.c)
        return disc

    def numberOfRoots(self):
     #  number = 1
        disc = self.discriminant()
        if disc < 0: 
            number = 0
        elif -1e-15 < disc < 1e-15:
            number = 1
        elif disc > 0:
            number = 2
    
        return number

    def roots(self):
        discriminant = self.discriminant()
        nOR = self.numberOfRoots()
        if nOR == 0:
            rootValues = None
            
        elif nOR == 1:
            n = -self.b + discriminant**0.5
            x = n / (2 * self.a) 
            rootValues = float(x)
        
        elif nOR == 2:
            n1 = -self.b + discriminant**0.5
            x1 = n1 / (2 * self.a) 
            n2 = -self.b - discriminant**0.5
            x2 = n2 / (2 * self.a) 
            rootValues = (x1, x2)
            
        return rootValues

    @staticmethod
    def solveRoots(coefficients):
        if len(coefficients) != 3:
            print('Not a quadratic, you need three coefficients')
            return None

        for x in coefficients:
            if not isinstance(x, (int, float)):
                print('Not a quadratic, the coefficients need to be numbers')
                return None

        q = Quadratic(coefficients[0], coefficients[1], coefficients[2])
        return q.roots()




