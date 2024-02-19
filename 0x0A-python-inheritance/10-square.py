#!/usr/bin/python3
"""A module for task 10."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class definition of a Square."""

    def __init__(self, size):
        """Square Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area of Square"""
        return self.__size**2
