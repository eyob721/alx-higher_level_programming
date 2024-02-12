#!/usr/bin/python3
"""Task 0"""


def add_integer(a, b=98) -> int:
    """Adds two integers

    Args:
        a (int | float): first integer
        b (int | float): second integer

    Returns:
        sum of `a` and `b`.

    Raises:
        TypeError: if either `a` or `b` are not int or float.

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
