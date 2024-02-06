#!/usr/bin/python3
"""Task 2 - test script"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Square = __import__("2-square").Square

my_square_1 = Square(3)
print("\nTest 1 ---------------------")
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print("\nTest 2 ---------------------")
print(type(my_square_2))
print(my_square_2.__dict__)

print("\nTest 3 ---------------------")
try:
    print(my_square_1.size)
except Exception as e:
    print(e)

print("\nTest 4 ---------------------")
try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

print("\nTest 5 ---------------------")
try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

print("\nTest 6 ---------------------")
try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
