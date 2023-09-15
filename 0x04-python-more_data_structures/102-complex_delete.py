#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    A function that deletes all keys in a dictionary that match with a given
    value.

    Args:
        a_dictionary: a dictionary
        value: given value

    Returns:
        - a copy of the modified dictionary
        - if `a_dictionary` is None, it returns None

    """
    if a_dictionary is not None:
        while value in a_dictionary.values():
            value_index = list(a_dictionary.values()).index(value)
            key = list(a_dictionary.keys())[value_index]
            del a_dictionary[key]
        return a_dictionary.copy()
