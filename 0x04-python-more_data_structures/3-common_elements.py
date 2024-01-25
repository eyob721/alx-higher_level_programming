#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    A function that returns a set of common elements in two elements

    Args:
        set_1: first set
        set_2: second set

    Returns:
        - a set of common elements
        - if either of set_1 or set_2 is None, it returns None

    """
    if set_1 is not None and set_2 is not None:
        return set_1 & set_2
