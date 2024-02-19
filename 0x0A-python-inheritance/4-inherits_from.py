#!/usr/bin/python3
"""Task 4"""


def inherits_from(obj, a_class):
    """Returns True if an object is an instance of a class that directly or
       indirectly inherited from the specified class.

    Note:
        It checks inheritance only. So it returns False if `obj` is an exact
        instance of `a_class`.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
