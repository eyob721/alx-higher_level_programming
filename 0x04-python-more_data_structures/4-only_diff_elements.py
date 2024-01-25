#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    A function that returns a set of all elements that are present in only one
    set and not both.

    Args:
        set_1: first set
        set_2: second set

    Returns:
        - a set of all elements that are present in only one set and not both.
        - if either of set_1 or set_2 is None, it returns None

    """
    if set_1 is not None and set_2 is not None:
        return set_1 ^ set_2
