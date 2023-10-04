#!/usr/bin/python3
"""A module for task 3.

This module contains the function `say_my_name()`.

"""


def say_my_name(first_name, last_name=""):
    """Prints first name and last name in a specific format.

    Args:
        first_name (str): First name
        last_name (str): Last name

    Returns:
        None

    Raises:
        TypeError: If either of `first_name` or `last_name` is not a string.

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
