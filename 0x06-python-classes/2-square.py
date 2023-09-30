#!/usr/bin/python3
"""A module for Task 2.

Description:
    - Building on the previous module (1-square.py), in this module we validate
      the size attribute, so that only an object of type int and a value
      of >= 0 is accepted as a valid size.
    - Otherwise it will raise TypeError and ValueError respectively.

"""


class Square:
    """A class that defines a Square object.

    Args:
        size: Initial size of the square object. It must be an integer and >= 0

    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
