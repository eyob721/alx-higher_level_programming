#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class definition of a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square"""
        sqr = f"[Square] ({self.id:d}) {self.x:d}/{self.y:d} - {self.width:d}"
        return sqr
