"""
A skeleton template for the Triangle class in Week 2: Coding Exercises.
"""

import math


class Triangle:
    """
    A class representing a triangle.

    Parameters
    ----------
    lengthSide1: (int, float)
        The length of the first side.
    lengthSide2: (int, float)
        The length of the second side.
    lengthSide3: (int, float)
        The length of the third side.
    """

    def __init__(self, lengthSide1, lengthSide2, lengthSide3):
        self.side1 = lengthSide1
        self.side2 = lengthSide2
        self.side3 = lengthSide3
       

        # Run test to check if triangle is valid
        if not self.testIfValidTriangle():
            raise ValueError(f"A triangle with sides ({self.side1}, "
                             f"{self.side2}, {self.side3}) is not valid")
        
    
    

    def __str__( self ):
        return f"Triangle (sides {self.side1}, {self.side2}, {self.side3})"

    def testIfValidTriangle(self):
        """Carry out checks that this is a triangle."""
        
        # all side lengths must be a float or an integer
        if not isinstance(self.side1, (int, float)):
            raise ValueError(f"A triangle with sides ({self.side1}, "
                             f"{self.side2}, {self.side3}) is not valid")
        if not isinstance(self.side2, (int, float)):
            raise ValueError(f"A triangle with sides ({self.side1}, "
                             f"{self.side2}, {self.side3}) is not valid")
        if not isinstance(self.side3, (int, float)):
            raise ValueError(f"A triangle with sides ({self.side1}, "
                             f"{self.side2}, {self.side3}) is not valid")
        
        # all side lengths must be positive
        sides = [self.side1, self.side2, self.side3]
        for i in sides:
            if i <= 0:
                test = False

        
        # the sum of 2 sides must not be greater than the length of the third side
        if self.side1 + self.side2 <= self.side3:
            test = False
        if self.side1 + self.side3 <= self.side2:
            test = False
        if self.side2 + self.side3 <= self.side1:
            test = False

        return test

    def calcTriangleArea(self):
        """Return area of the triangle."""
        return area


