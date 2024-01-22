#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

add_tuple = __import__("7-add_tuple").add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)

new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1,)))
print(add_tuple(tuple_a, ()))

print(add_tuple((1, 2, 3, 5), (9, 7, 5, 7, 10)))
print(add_tuple(None, None))
