#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function that replaces an item in a list, without modifying the
       original list.

       The function copies the original list. And based on the value of `idx`
       it modifies it.

    Args:
        my_list: a given list
        idx: index of the member in `my_list` to replace
        element: element to replace the member at `my_list[idx]`

    Return:
        - If `idx` is negative or out of range, it returns a copy of the
          original list.
        - Otherwise it returns a copy of 'my_list' with the element at `idx`
          replaced.
    """
    new_list = my_list.copy()
    if 0 <= idx < len(my_list):
        new_list[idx] = element
    return new_list
