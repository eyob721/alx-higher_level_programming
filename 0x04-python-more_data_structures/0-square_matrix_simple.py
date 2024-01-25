#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """A function that computes the square value of all integers of a matrix

    Args:
        matrix: a given matrix, default value is an empty list

    Returns:
        - if matrix is None or empty, returns None
        - otherwise, returns a new squared matrix

    """
    return [[x**2 for x in row] for row in matrix] if matrix else None
