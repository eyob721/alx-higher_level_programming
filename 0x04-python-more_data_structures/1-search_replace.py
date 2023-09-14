#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences of an element in a list by
    another element

    Args:
        my_list: a given list
        search: element to search for
        replace: element to replace with

    Returns:
        - a new list with the `search` element replaced by the `replace`
          element.
        - if `my_list` is None or empty, it returns None

    """
    if my_list:
        return list(map(lambda x: replace if x == search else x, my_list))
