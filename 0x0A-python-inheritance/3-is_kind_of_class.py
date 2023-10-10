#!/usr/bin/python3
"""A module for task 3."""


def is_kind_of_class(obj, a_class):
    """Returns True if an object is a subclass of a class."""
    return issubclass(type(obj), a_class)
