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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """X position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the Rectangle in stdout using the `#` character"""
        rectangle = (("#" * self.__width + "\n") * self.__height).rstrip("\n")
        print(rectangle)

    def __str__(self):
        """Informal string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )
