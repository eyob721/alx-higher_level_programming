#!/usr/bin/python3
"""Task 0 - test script"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Square = __import__("0-square").Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
