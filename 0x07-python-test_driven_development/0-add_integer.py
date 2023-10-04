#!/usr/bin/python3
"""A module for Task 0.

This module contains only the function `add_integer`.

"""


def add_integer(a, b=98):
    """Adds two integers.

    Note:
        The values `a` and `b` are first casted into integers.

    Args:
        a (int | float): First integer
        b (int | float): Second integer

    Returns:
        Sum of `a` and `b`.

    Raises:
        TypeError: If either `a` or `b` are not int or float.

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
