#!/usr/bin/python3
"""Task 7"""


def safe_print_integer_err(value):
    """Prints an integer.

    Args:
        value: an object of any type

    Returns:
        - True if it has printed an integer, False otherwise.

    """
    import sys

    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    return True
