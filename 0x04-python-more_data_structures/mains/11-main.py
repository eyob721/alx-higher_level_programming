#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

multiply_list_map = __import__("11-multiply_list_map").multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
print("--")
my_list = []
new_list = multiply_list_map(my_list, 7)
print(new_list)
print(my_list)
