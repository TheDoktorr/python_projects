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
        test = True
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
        a = self.side1
        b = self.side2
        c = self.side3
        s = 0.5 * (a + b + c)
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        if area <= 0:
            raise ValueError(f"A triangle with sides ({self.side1}, "
                             f"{self.side2}, {self.side3}) is not valid")

        return area


# Testing code
triangles_to_test = [
    (3, 4, 5),  # valid triangle
    (1, 1, 2),  # invalid triangle (sum of two sides equals the third side)
    (0, 4, 5),  # invalid triangle (one side is zero)
    (-3, 4, 5), # invalid triangle (one side is negative)
    (3, 3, 5),  # valid triangle
]

for sides in triangles_to_test:
    try:
        triangle = Triangle(*sides)
        area = triangle.calcTriangleArea()
        print(f"Triangle with sides {sides} is valid, area: {area}")
    except ValueError as e:
        print(f"Error: {e}")

