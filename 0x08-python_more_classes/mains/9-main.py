#!/usr/bin/python3
"""Main script for Task 9"""
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Rectangle = __import__("9-rectangle").Rectangle

my_square = Rectangle.square(5)
print("Width: {} - Height: {}".format(my_square.width, my_square.height))
print(
    "Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter())
)
print(my_square)
