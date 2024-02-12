#!/usr/bin/python3
"""Task 6

This module contains the functions:
    `matrix_mul`: multiplies 2 matrices
    `validate_matrix`: validates a matrix
    `check_mul_compatibility`: checks if two matrices are compatible
                               for multiplication

"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices.

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        product of the two matrices

    """
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")
    check_mul_compatibility(m_a, m_b)
    row_b = len(m_b)
    col_b = len(m_b[0])
    result = []
    for row in m_a:
        col = 0
        result_row = []
        while col < col_b:
            i = j = prdt_sum = 0
            while j < row_b:
                prdt_sum += row[i] * m_b[j][col]
                i += 1
                j += 1
            result_row.append(prdt_sum)
            col += 1
        result.append(result_row)
    return result


def validate_matrix(matrix, name):
    """A function used to validate a matrix

    Args:
        matrix: the matrix
        name: name of the matrix

    Raises:
        TypeError:
            If either of the matrices are not lists, or are not list of lists
            If the matrices contain types other than int or float
            If the matrices contain rows of different sizes
        ValueError:
            If the matrices contain empty lists

    """
    # 1: Check for type of matrix
    if type(matrix) is not list:
        raise TypeError(f"{name} must be a list")
    # 2: Check for type of rows
    for row in matrix:
        if type(row) is not list:
            raise TypeError(f"{name} must be a list of lists")
    # 3: Check for empty matrices and empty rows
    if len(matrix) == 0:
        raise ValueError(f"{name} can't be empty")
    for row in matrix:
        if len(row) == 0:
            raise ValueError(f"{name} can't be empty")
    # 4: Check for types of elements in the row
    err_msg = f"{name} should contain only integers or floats"
    for row in matrix:
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError(err_msg)
    # 5: Check for size of rows
    err_msg = f"each row of {name} must be of the same size"
    total_row_size = 0
    for row in matrix:
        row_size = len(row)
        total_row_size += row_size
        if row_size != 0 and total_row_size % row_size != 0:
            raise TypeError(err_msg)


def check_mul_compatibility(m_a, m_b):
    """Checks it 2 matrices are compatible for multiplication."""
    col_a = len(m_a[0])
    row_b = len(m_b)
    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")
