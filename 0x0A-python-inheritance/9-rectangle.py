#!/usr/bin/python3
"""Task 9"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class definition of a Rectangle."""

    def __init__(self, width, height):
        """Rectangle Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation of Rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
