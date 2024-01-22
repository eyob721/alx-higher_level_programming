#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """A function that adds the first two elements of two tuples of integers.

    Args:
        tuple_a: first tuple
        tuple_b: second tuple

    Returns:
        - A tuple with 2 integers where:
        - The first element is the sum of the first elements of both tuples
        - The second element is the sum of the second elements of both tuples

    """
    sums = [0, 0]

    # Add the first elements of tuple_a and tuple_b
    sums[0] = 0 if tuple_a is None or len(tuple_a) == 0 else tuple_a[0]
    sums[0] += 0 if tuple_b is None or len(tuple_b) == 0 else tuple_b[0]

    # Add the second elements of tuple_a and tuple_b
    sums[1] = 0 if tuple_a is None or len(tuple_a) <= 1 else tuple_a[1]
    sums[1] += 0 if tuple_b is None or len(tuple_b) <= 1 else tuple_b[1]

    return tuple(sums)
