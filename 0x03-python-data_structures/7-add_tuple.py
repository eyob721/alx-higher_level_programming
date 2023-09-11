#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ A function that adds two tuples of integers.

    Only the first two integers are added.
    If a tuple is smaller than 2, then a value of 0 is used for each missing
    integers. Else if a tuple is larger than 2, then only the first 2 elements
    are added.

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        - A tuple with 2 integers
        - The first element is the sum of the first elements in both tuples
        - The second element is the sum of the second elements in both tuples

    """
    list_sum = [0, 0]
    if tuple_a is not None or tuple_b is not None:
        add_tuple_to_list_sum(tuple_a, list_sum)
        add_tuple_to_list_sum(tuple_b, list_sum)
    return tuple(list_sum)


def add_tuple_to_list_sum(tuple_x, list_sum):
    """ A function that adds the first two integers of `tuple_x` to `list_sum`

    Args:
        tuple_x: a given tuple

    Returns:
        None

    """
    tup_len = len(tuple_x)
    extent = tup_len if tup_len < 2 else 2
    for i in range(extent):
        list_sum[i] += tuple_x[i]
