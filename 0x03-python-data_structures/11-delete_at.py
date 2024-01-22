#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """A function that deletes the item at a specific position in a list

    Args:
        my_list: a given list
        idx: index of the item in `my_list` to delete

    Returns:
        - A modified list.
        - If idx is negative or out of range, nothing is changed.

    """
    if my_list is not None and 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
