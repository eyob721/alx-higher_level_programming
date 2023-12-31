#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    A function that prints an integer.

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
