#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """A function that replaces an item in a list

    Args:
        my_list: a given list
        idx: index of the member in `my_list` to replace
        element: element to replace the member at `my_list[idx]`

    Return:
        - If `idx` is negative or out of range, it returns the original list.
        - Otherwise it returns a modified 'my_list'
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
