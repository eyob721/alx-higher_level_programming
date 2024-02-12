#!/usr/bin/python3
"""Main script for Task 5"""
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Rectangle = __import__("5-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print(
    "Area: {} - Perimeter: {}".format(
        my_rectangle.area(), my_rectangle.perimeter()
    )
)

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
