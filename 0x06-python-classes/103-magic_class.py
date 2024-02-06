#!/usr/bin/python3
"""Task 10"""
import math


class MagicClass:
    """Class definition derived from given Bytecode"""

    def __init__(self, radius=0):
        """Magic Class constructor"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area of the Magic Class :)"""
        return (self.__radius**2) * math.pi

    def circumference(self):
        """Circumference of the Magic Class :)"""
        return 2 * math.pi * self.__radius
