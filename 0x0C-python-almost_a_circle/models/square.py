#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class definition of a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
        self.__size = size

    def __str__(self):
        """String representation of the Square"""
        sqr = f"[Square] ({self.id:d}) {self.x:d}/{self.y:d} - {self.width:d}"
        return sqr
