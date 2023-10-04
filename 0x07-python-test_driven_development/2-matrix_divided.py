#!/usr/bin/python3
"""A module for task 1.

The module contains the function `matrix_divided()`.

"""


def matrix_divided(matrix, div):
    """Divides a matrix by a given number.

    Args:
        matrix: A list of lists of integers/floats.
        div: The dividing number.

    Returns:
        A new list containing the result of the division,
        rounded to 2 decimal places.

    Raises:
        TypeError: When the matrix contains row of different sizes, or
                   when the row is not a list, or
                   when the elements in the row are not integers or floats.
        ZeroDivisionError: When the `div` argument is zero.

    """
    type_err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_err_msg = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(type_err_msg)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    total_row_size = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(type_err_msg)
        row_size = len(row)
        total_row_size += row_size
        if row_size != 0 and total_row_size % row_size != 0:
            raise TypeError(size_err_msg)
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError(type_err_msg)
    return [[round(x / div, 2) for x in row] for row in matrix]
