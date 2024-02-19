#!/usr/bin/python3
"""A module for task 13."""


def add_attribute(obj, name, value):
    """Adds an attribute to an object, if it's possible.

    Args:
        obj (obj): object
        name (str): name of the attribute
        value (str): value of the attribute

    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
