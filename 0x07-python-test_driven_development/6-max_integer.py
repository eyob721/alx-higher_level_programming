#!/usr/bin/python3
"""Task 5"""


def max_integer(list=[]):
    """Finds and returns the max integer in a list of integers

    Args:
        list (list): a list of integers

    Returns:
        maximum integer

    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
