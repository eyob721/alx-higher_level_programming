#!/usr/bin/python3
"""Main script for Task 3"""
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Rectangle = __import__("3-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print("Width: {} - Height: {}".format(my_rectangle.width, my_rectangle.height))
print(
    "Area: {} - Perimeter: {}".format(
        my_rectangle.area(), my_rectangle.perimeter()
    )
)

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Width: {} - Height: {}".format(my_rectangle.width, my_rectangle.height))

print(my_rectangle)
print(repr(my_rectangle))
