#!/usr/bin/python3
"""A module for Task 1.

Description:
    In this module we add the private instance attribute `size` to the Square
    class from Task 0.

"""


class Square:
    """A class that defines a Square object.

    Args:
        size: initial size of the square object

    """
    def __init__(self, size):
        self.__size = size
