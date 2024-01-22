#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

max_integer = __import__("9-max_integer").max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]

max_value = max_integer(my_list)
print("Max: {}".format(max_value))

max_value = max_integer([])
print("Max: {}".format(max_value))

max_value = max_integer(None)
print("Max: {}".format(max_value))
