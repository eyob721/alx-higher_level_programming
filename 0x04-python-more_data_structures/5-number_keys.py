#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    A function that returns the number of keys in a dictionary.

    Args:
        a_dictionary: a dictionary

    Returns:
        - number of keys in a dictionary
        - if `a_dictionary` is None, it returns None

    """
    return len(a_dictionary.keys()) if a_dictionary is not None else None
