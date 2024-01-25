#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

square_matrix_map = __import__("101-square_matrix_map").square_matrix_map

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)
