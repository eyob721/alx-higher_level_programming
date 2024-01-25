#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary with all the values
    multiplied by 2. It is assumed that all the values are integers.

    Args:
        a_dictionary: a dictionary

    Returns:
        - a new dictionary with the values multiplied by 2
        - if the given dictionary is None, it returns None

    """
    if a_dictionary is not None:
        return {x: a_dictionary[x] * 2 for x in a_dictionary.keys()}
