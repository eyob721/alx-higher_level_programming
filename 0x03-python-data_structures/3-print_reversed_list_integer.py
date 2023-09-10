#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers from a list, in reverse order

    The function assumes that list contains integers only, and so each integer
    is printed on a single line, in integer format.

    Args:
        my_list: given list of integers

    Returns:
        None

    """
    idx = len(my_list) - 1
    while (idx >= 0):
        print("{:d}".format(my_list[idx]))
        idx -= 1
