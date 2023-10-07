#!/usr/bin/python3
"""A module for task 7.

This module contains the functions:
    `lazy_matrix_mul`: multiplies 2 matrices using the numpy module

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using the numpy module.

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        Product of the two matrices.

    """
    # 1: Check for type of matrices
    if type(m_a) is not list or type(m_b) is not list:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # 2: Check for empty matrices and empty rows
    h_a = len(m_a)
    w_a = 0 if h_a == 0 else len(m_a[0])
    h_b = len(m_b)
    w_b = 0 if h_b == 0 else len(m_b[0])
    err_msg1 = f"shapes ({w_b:d}, {h_a:d}) and ({w_b:d}, {w_b:d}) not "
    err_msg2 = f"aligned: {h_a:d} (dim {h_b:d}) != {w_b:d} (dim {h_a:d})"
    if h_a == 0 or w_a == 0 or h_b == 0 or w_b == 0:
        raise ValueError(err_msg1 + err_msg2)

    # 3: Check for size of rows and types of elements in the rows
    for r_a in m_a:
        if type(r_a) is not list:
            raise ValueError("Scalar " +
                             "operands are not allowed, use '*' instead")
        if len(r_a) != len(m_a[0]):
            raise ValueError("setting an array element with a sequence.")
        for c_a in r_a:
            if type(c_a) not in [int, float]:
                raise TypeError("invalid data type for einsum")

    for r_b in m_b:
        if type(r_b) is not list:
            raise ValueError("Scalar " +
                             "operands are not allowed, use '*' instead")
        if len(r_b) != len(m_b[0]):
            raise ValueError("setting an array element with a sequence.")
        for c_b in r_b:
            if type(c_b) not in [int, float]:
                raise TypeError("invalid data type for einsum")

    # 5: Check for multiplication compatibility
    if w_a != h_b:
        raise ValueError(err_msg1 + err_msg2)

    # 6: Return dot product
    return np.dot(m_a, m_b)
