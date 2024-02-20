#!/usr/bin/python3
"""Task 12"""


def pascal_triangle(n):
    """Returns list of lists of integers representing the Pascal's triangle."""
    triangle = [[1] * i for i in range(1, n + 1)]
    for i in range(1, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle
