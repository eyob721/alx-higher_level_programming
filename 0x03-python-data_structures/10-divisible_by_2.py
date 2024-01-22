#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """A function that finds all multiples of 2 in a list

    Args:
        my_list: a given list of integers

    Returns:
        - A new list with `True` or `False`, depending on whether the integer
          at the same position in the original list is a multiple of 2

    """
    if my_list is not None:
        return [bool(x % 2 == 0) for x in my_list]
