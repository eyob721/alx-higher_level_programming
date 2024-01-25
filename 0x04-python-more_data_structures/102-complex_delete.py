#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes all keys in a dictionary that matchs a given value.

    Args:
        a_dictionary: a dictionary
        value: given value

    Returns:
        - a copy of the modified dictionary
        - if `a_dictionary` is None, it returns None

    """
    if a_dictionary is not None:
        for key in list(a_dictionary.keys()):
            if value == a_dictionary.get(key):
                del a_dictionary[key]
        return a_dictionary.copy()
