#!/usr/bin/python3
def max_integer(my_list=[]):
    """ A function that finds the maximum integer in a list

    Args:
        my_list: a list of integers

    Returns:
        - The maximum integer in 'my_list'
        - If `my_list` is empty or None, then it will return None

    """
    if my_list:
        max_int = 0
        for i in my_list:
            if i > max_int:
                max_int = i
        return max_int
