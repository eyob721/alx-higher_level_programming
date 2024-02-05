#!/usr/bin/python3
"""Main script for task 8"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

safe_function = __import__("101-safe_function").safe_function


def my_div(a, b):
    """Divides a by b"""
    return a / b


result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    """Prints a list"""
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len


result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))
