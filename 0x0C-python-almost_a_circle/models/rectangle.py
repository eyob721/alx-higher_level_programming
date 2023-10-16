#!/usr/bin/python3
"""This module contains the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Class definition of a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width of the Rectangle"""
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
        """x position of the Rectangle"""
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
        """y position of the Rectangle"""
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
        return self.width * self.height

    def display(self):
        """Displays the Rectangle on stdout using `#` character."""
        rec_output = '\n' * self.y
        rec_output += ((' ' * self.x + '#' * self.width + '\n') * self.height)
        print(rec_output.rstrip('\n'))

    def __str__(self):
        """String representation of the Rectangle"""
        rec_str = f"[Rectangle] ({self.id:d}) {self.x:d}/{self.y:d}" +\
            f" - {self.width:d}/{self.height:d}"
        return rec_str

    def update(self, *args, **kwargs):
        """Updates the Rectangle's attributes.
        If `*args` is given, `**kwargs` is skipped
        """
        rec_attr = ['id', 'width', 'height', 'x', 'y']
        i = 0
        for arg in args:
            setattr(self, rec_attr[i], arg)
            i += 1
            if i == 5:  # 5 == len(rec_attr)
                break
        if not args:
            for key in kwargs:
                if key in rec_attr:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        rec_attr = ['id', 'width', 'height', 'x', 'y']
        rec_dict = {key: getattr(self, key) for key in rec_attr}
        return rec_dict
