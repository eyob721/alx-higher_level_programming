#!/usr/bin/python3
"""Task 1"""


def matrix_divided(matrix, div):
    """Divides a matrix by a given number.

    Args:
        matrix (list[list[int | float]]): A list of lists of integers/floats.
        div (int | float): The dividing number.

    Returns:
        A new list containing the result of the division,
        rounded to 2 decimal places.

    Raises:
        TypeError: when the matrix contains row of different sizes, or
                   when the row is not a list, or
                   when the elements in the row are not integers or floats.
        ZeroDivisionError: when the `div` argument is zero.

    """
    type_err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_err_msg = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(type_err_msg)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = (
        len(matrix[0]) if matrix != [] and type(matrix[0]) is list else 0
    )
    for row in matrix:
        # Check type of row
        if type(row) is not list:
            raise TypeError(type_err_msg)

        # Check size of row
        if len(row) != row_size:
            raise TypeError(size_err_msg)

        # Check type of row elements
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError(type_err_msg)

    return [[round(x / div, 2) for x in row] for row in matrix]
