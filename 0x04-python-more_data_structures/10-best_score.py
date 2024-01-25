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
        max_score_idx = list(a_dictionary.values()).index(max_score)
        return list(a_dictionary.keys())[max_score_idx]
