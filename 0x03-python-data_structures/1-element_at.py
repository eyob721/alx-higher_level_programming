#!/usr/bin/python3
def element_at(my_list, idx):
    """A function that retrieves an element from a list

    Args:
        my_list: a list
        idx: index of the item to retrieve

    Returns:
        - If `idx` is less than 0 or is out of range, it returns None
        - Otherwise it returns an element at index `idx` of `my_list`

    """
    return my_list[idx] if 0 <= idx < len(my_list) else None
