#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    A function that prints `x` elements from `my_list`

    Args:
        my_list: a given list
        x: number of elements to print

    Returns:
        - number of items printed

    """
    printed = i = 0
    try:
        while i < x:
            print("{}".format(my_list[i]), end="")
            printed = i = i + 1
    except Exception:
        pass
    print()
    return printed
