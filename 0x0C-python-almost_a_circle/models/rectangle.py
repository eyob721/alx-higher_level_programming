#!/usr/bin/python3
"""Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x position of the rectangle
        y (int): y position of the rectangle

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x position of the rectangle
            y (int): y position of the rectangle
            id (int): id of the rectangle

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """X position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """Y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
