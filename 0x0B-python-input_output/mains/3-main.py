#!/usr/bin/python3
"""Task 3"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

to_json_string = __import__("3-to_json_string").to_json_string

print("--- list to JSON ---")
my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))
print("--------------------")

print("--- dict to JSON ---")
my_dict = {
    "id": 12,
    "name": "John",
    "places": ["San Francisco", "Tokyo"],
    "is_active": True,
    "info": {"age": 36, "average": 3.14},
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))
print("--------------------")

print("--- set to JSON ---")
try:
    my_set = {132, 3}
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
print("-------------------")

print("--- bytes to JSON ---")
try:
    my_byte = b"1001"
    s_my_byte = to_json_string(my_byte)
    print(s_my_byte)
    print(type(s_my_byte))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
print("---------------------")
