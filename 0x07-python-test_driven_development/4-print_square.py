#!/usr/bin/python3
"""Task 3"""


def print_square(size):
    """Prints a square of given size, using the `#` character

    Args:
        size (int): size of the square

    Returns:
        None

    Raises:
        TypeError: if `size` is not an integer
        ValueError: if `size` is < 0

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    square = ("#" * size + "\n") * size
    print(square, end="")
