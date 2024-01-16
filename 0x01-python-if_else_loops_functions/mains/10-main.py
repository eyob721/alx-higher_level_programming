#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

add = __import__("10-add").add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
