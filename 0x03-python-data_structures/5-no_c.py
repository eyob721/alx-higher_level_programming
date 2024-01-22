#!/usr/bin/python3
def no_c(my_string):
    """
    A function that removes all characters 'c' and 'C' from a string

    Args:
        my_string: a given string

    Returns:
        - The new string, or
        - If `my_string` is None or empty, it returns `my_string`

    """
    if my_string:
        return "".join([ch for ch in my_string if ch != "c" and ch != "C"])
    return my_string
