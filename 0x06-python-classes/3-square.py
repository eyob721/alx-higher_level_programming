#!/usr/bin/python3
"""Task 3"""


class Square:
    """A class that defines a Square object"""

    def __init__(self, size=0):
        """Square constructor

        Args:
            size: Initial size of the square object
                  It must be an integer and >= 0.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the square object

        Returns:
            int: Area of the square object.

        """
        return self.__size * self.__size
