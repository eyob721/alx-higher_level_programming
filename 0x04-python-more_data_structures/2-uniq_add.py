#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    A function that adds all unique integers in a list.

    Args:
        my_list: a given list of integers

    Returns:
        - A sum of all the unique integers in a list.
        - If `my_list` is None, it returns None

    """
    if my_list is not None:
        uniq_ints = list(set(my_list))
        return sum(uniq_ints)
