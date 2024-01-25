#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

update_dictionary = __import__("7-update_dictionary").update_dictionary
print_sorted_dictionary = __import__(
    "6-print_sorted_dictionary"
).print_sorted_dictionary

a_dictionary = {"language": "C", "number": 89, "track": "Low level"}
print("Originally:")
print_sorted_dictionary(a_dictionary)
print()

new_dict = update_dictionary(a_dictionary, "language", "Python")
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print()

new_dict = update_dictionary(a_dictionary, "city", "San Francisco")
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
