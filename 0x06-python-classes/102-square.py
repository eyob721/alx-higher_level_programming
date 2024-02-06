#!/usr/bin/python3
"""Task 9"""


class Square:
    """A class that defines a Square object"""

    def __init__(self, size=0):
        """Square constructor

        Args:
            size: Initial size of the square object
                  It must be an integer and >= 0

        """
        self.size = size

    @property
    def size(self):
        """Size of the square object"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square object

        Returns:
            int: Area of the square object

        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Overrides the == relational operator

        Args:
            other: The second operand object in the comparison

        Returns:
            True if other is a Square object and its area is == with the
            current object area. False otherwise.

        """
        return self.area() == other.area()

    def __lt__(self, other):
        """Overrides the < relational operator

        Args:
            other: The second operand object in the comparison

        Returns:
            True if other is a Square object and its area is < the current
            object area. False otherwise.

        """
        return self.area() < other.area()

    def __le__(self, other):
        """Overrides the <= relational operator

        Args:
            other: The second operand object in the comparison

        Returns:
            True if other is a Square object and its area is <= the current
            object area. False otherwise.

        """
        return self.area() <= other.area()
