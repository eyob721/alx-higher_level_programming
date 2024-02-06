#!/usr/bin/python3
"""Task 5 - test script"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Square = __import__("5-square").Square

print("\nTest 1 ---------------------")
my_square = Square(3)
my_square.my_print()

print("--")

print("\nTest 2 ---------------------")
my_square.size = 10
my_square.my_print()

print("--")

print("\nTest 3 ---------------------")
my_square.size = 0
my_square.my_print()

print("--")
