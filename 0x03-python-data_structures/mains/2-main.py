#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

replace_in_list = __import__("2-replace_in_list").replace_in_list

my_list = [1, 2, 3, 4, 5]
print(f"Original: {my_list}\n")

idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print("After valid replacment, there should be a change")
print(new_list)
print(my_list)

idx = -1
new_element = 55
new_list = replace_in_list(my_list, idx, new_element)
print("After invalid replacment, there should be no change")
print(new_list)
print(my_list)

idx = 10
new_element = 55
new_list = replace_in_list(my_list, idx, new_element)
print("After invalid replacment, there should be no change")
print(new_list)
print(my_list)
