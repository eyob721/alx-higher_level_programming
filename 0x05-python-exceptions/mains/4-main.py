#!/usr/bin/python3
"""Main script for task 4"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

list_division = __import__("4-list_division").list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
