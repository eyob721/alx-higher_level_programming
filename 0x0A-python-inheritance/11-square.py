#!/usr/bin/python3
"""Task 11"""

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

    def __str__(self):
        """String representation of Square"""
        return f"[Square] {self.__size}/{self.__size}"
