#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

print_reversed_list_integer = __import__(
    "3-print_reversed_list_integer"
).print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
print()

my_list = [12, 6, 55, 32]
print_reversed_list_integer(my_list)
print()

my_list = []
print_reversed_list_integer(my_list)
print()
