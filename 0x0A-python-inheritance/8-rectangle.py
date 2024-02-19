#!/usr/bin/python3
"""Task 8"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class definition of a Rectangle."""

    def __init__(self, width, height):
        """Rectangle Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
