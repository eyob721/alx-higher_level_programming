#!/usr/bin/python3
"""Task 1"""


def safe_print_integer(value):
    """A function that prints an integer with `{:d}.format()`.

    Args:
        value: an object of any data type

    Returns:
        - True, if the object is printed
        - False, if the object is not printed
    """
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    return True
