#!/usr/bin/python3
"""Task 2"""


def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x items from a list, that are only integers.

    Args:
        my_list: a given list
        x: number of elements to print

    Returns:
        - the number of elements printed
    """
    printed = i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (TypeError, ValueError):
            pass
        i += 1
    print()
    return printed
