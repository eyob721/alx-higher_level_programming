#!/usr/bin/python3
"""Task 12"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

pascal_triangle = __import__("12-pascal_triangle").pascal_triangle


def print_triangle(triangle):
    """Print the triangle"""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
    print("---")


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
    print_triangle(pascal_triangle(7))
    print_triangle(pascal_triangle(10))
