#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a matrix of integers

    Args:
        matrix: a given matrix, defaults to [[]]

    Returns:
        None

    """
    if matrix:
        for row in matrix:
            row_len = len(row)
            for i in range(row_len):
                print("{:d}".format(row[i]), end="")
                if i < row_len - 1:
                    print(" ", end="")
            print()
