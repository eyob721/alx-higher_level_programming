#!/usr/bin/python3
"""A module that solves the `N queens` problem."""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)

queen = [[i, 0] for i in range(N)]
"""A list that contains the place of each queen on the board.
Initially each queen is placed on the first column of each row.
"""


def print_board():
    """Utility function to display the chess board"""
    print("### BOARD ###")
    for row in range(N):
        for col in range(N):
            if [row, col] == queen[row]:
                print("[Q]", end="")
            else:
                print("[-]", end="")
        print()
    print()


def queen_is_column_safe(q):
    """Utility function to check if a queen is on a safe column.

    Args:
        q (list): The queen.
        row (int): The row that the queen is on

    Returns
        bool: True if she is safe, False if not.

    """
    # Column safety check
    for row in range(q[0]):
        if q[1] == queen[row][1]:
            return False
    return True


def queen_is_diagonal_safe(q):
    """Utility function to check if a queen is on a safe diagonally.

    Args:
        q (list): The queen.

    Returns
        bool: True if she is safe, False if not.

    """
    # Check upper left
    row, col = q
    while True:
        row, col = row - 1, col - 1
        if not (0 <= row < N and 0 <= col < N):
            break
        if queen[row][1] == col:
            return False
    # Check upper right
    row, col = q
    while True:
        row, col = row - 1, col + 1
        if not (0 <= row < N and 0 <= col < N):
            break
        if queen[row][1] == col:
            return False
    return True


def queen_is_safe(q):
    """Overall check"""
    return queen_is_column_safe(q) and queen_is_diagonal_safe(q)


def solve_nqueens():
    """Function to solve the nqueens problem."""
    all_safe = False
    result = []
    for col in range(N):
        queen[0][1] = col
        all_safe = solve_next_queen(1)
        if all_safe:
            print(queen)
    return result


def solve_next_queen(row):
    if row == N:
        return True
    next_is_safe = False
    for col in range(N):
        queen[row][1] = col
        if queen_is_safe(queen[row]):
            next_is_safe = solve_next_queen(row + 1)
            if next_is_safe:
                return True
    return False


if __name__ == "__main__":
    result = solve_nqueens()
