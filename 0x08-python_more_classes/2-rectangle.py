#!/usr/bin/python3
"""Task 2"""


class Rectangle:
    """Class definition of a Rectangle

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        area (int): area of the rectangle
        perimeter (int): perimeter of the rectangle

    """

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value) -> None:
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """Area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Perimeter of the Rectangle"""
        return (
            0
            if self.__width == 0 or self.__height == 0
            else 2 * (self.__width + self.__height)
        )
