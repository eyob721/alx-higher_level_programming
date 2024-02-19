#!/usr/bin/python3
"""Task 10 main script"""
import os
import sys

cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)

Square = __import__("10-square").Square

s = Square(13)

print(s)
print(s.area())
