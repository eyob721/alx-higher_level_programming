#!/usr/bin/python3
"""Task 3"""


def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a: first integer
        b: second integer

    Returns:
        - It returns the result of the division of `a` and `b`.
        - If there is a zero division it returns None.

    Note:
        - It is assumed that both `a` and `b` are integers.
    """
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res
