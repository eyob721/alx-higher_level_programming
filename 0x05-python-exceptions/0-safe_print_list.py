#!/usr/bin/python3
"""Task 0"""


def safe_print_list(my_list=[], x=0):
    """A function that prints x elements from a list

    Args:
        my_list: a given list
        x: number of elements to print

    Returns:
        - number of items printed
    """
    i = 0
    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            i += 1
    except Exception:
        pass
    print()
    return i
