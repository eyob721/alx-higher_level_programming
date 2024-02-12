#!/usr/bin/python3
"""Task 10: A module that solves the `N queens` problem."""

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
                print("[ ]", end="")
        print()
    print()


def queen_is_column_safe(q):
    """Check if a queen is safe column wise from the upper queens."""
    # Check columns of queens above the current queen
    for row in range(q[0]):
        if q[1] == queen[row][1]:
            return False
    return True


def queen_is_diagonal_safe(q):
    """Check if a queen is safe diagonally from the upper queens."""
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


def solve_nqueens(row=0):
    """Function to solve the nqueens problem."""
    if row == N:
        print(queen)
        return True
    for col in range(N):
        queen[row][1] = col
        if queen_is_safe(queen[row]):
            solve_nqueens(row + 1)
    return False


if __name__ == "__main__":
    solve_nqueens()
