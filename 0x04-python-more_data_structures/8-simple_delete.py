#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    A function that deletes a key in a dictionary.

    Args:
        a_dictionary: a dictionary
        key: key to delete

    Returns:
        - a copy of the modified dictionary
        - if `a_dictionary` is None, it returns None
        - if 'key' is None or empty, it returns None

    """
    if a_dictionary is not None and key:
        if key in a_dictionary:
            del a_dictionary[key]
        return a_dictionary.copy()
