#!/usr/bin/python3
def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.

    Args:
        a_dictionary: a dictionary

    Returns:
        - the key with the biggest integer value
        - if the given dictionary is empty or None, it returns None

    """
    if a_dictionary:
        max_score = sorted(a_dictionary.values())[-1]
        for key in a_dictionary.keys():
            if a_dictionary[key] == max_score:
                return key
