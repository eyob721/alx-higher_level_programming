#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    A function that replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: a dictionary
        key: an existing key to be replaced, or a new key to be inserted
        value: a new value for the key

    Returns:
        - a copy of the update dictionary
        - if either `a_dictionary` or `key` is None, it returns None

    """
    if a_dictionary and key:
        a_dictionary[key] = value
        return a_dictionary.copy()
