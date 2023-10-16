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
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """String representation of the Square"""
        sqr_str = f"[Square] ({self.id:d}) {self.x:d}/{self.y:d}" + \
            f" - {self.size:d}"
        return sqr_str

    def update(self, *args, **kwargs):
        """Updates the Square's attributes.
        Note:
            If `*args` is given, `**kwargs` is skipped
        """
        sqr_attr = ['id', 'size', 'x', 'y']
        i = 0
        for arg in args:
            setattr(self, sqr_attr[i], arg)
            i += 1
            if i == 4:  # 4 == len(sqr_attr)
                break
        if not args:
            for key in kwargs:
                if key in sqr_attr:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        sqr_attr = ['id', 'size', 'x', 'y']
        sqr_dict = {key: getattr(self, key) for key in sqr_attr}
        return sqr_dict
