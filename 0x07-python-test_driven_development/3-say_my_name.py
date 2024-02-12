#!/usr/bin/python3
"""Task 2"""


def say_my_name(first_name, last_name=""):
    """Prints first name and last name in a specific format

    Args:
        first_name (str): first name
        last_name (str): last name

    Returns:
        None

    Raises:
        TypeError: if either of `first_name` or `last_name` is not a string

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
