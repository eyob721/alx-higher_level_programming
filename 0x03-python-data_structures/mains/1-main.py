#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

element_at = __import__("1-element_at").element_at

my_list = [1, 2, 3, 4, 5]

idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

idx = -1
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

idx = 5
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
