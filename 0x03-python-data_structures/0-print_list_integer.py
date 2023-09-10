#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers from a list

    The function assumes that list contains integers only, and so each integer
    is printed on a single line, in integer format.

    Args:
        my_list: given list of integers

    Returns:
        None

    """
    for i in my_list:
        print("{:d}".format(i))
