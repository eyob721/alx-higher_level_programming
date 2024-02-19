#!/usr/bin/python3
"""Task 9 main script"""
import os
import sys

cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)

Rectangle = __import__("9-rectangle").Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())
