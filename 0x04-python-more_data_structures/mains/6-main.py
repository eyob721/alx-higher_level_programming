#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

print_sorted_dictionary = __import__(
    "6-print_sorted_dictionary"
).print_sorted_dictionary

a_dictionary = {
    "language": "C",
    "Number": 89,
    "track": "Low level",
    "ids": [1, 2, 3],
}
print_sorted_dictionary(a_dictionary)
