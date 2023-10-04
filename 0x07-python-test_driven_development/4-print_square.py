#!/usr/bin/python3
"""A module for task 3.

This module contains the function `print_square()`.

"""


def print_square(size):
    """Prints a square of given size, using the `#` character

    Args:
        size (int): Size of the square

    Returns:
        None

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is < 0.

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    square = "\n" if size == 0 else (('#' * size) + '\n') * size
    print(square, end="")
