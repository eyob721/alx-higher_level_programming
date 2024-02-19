#!/usr/bin/python3
"""Task 12 main script"""
import os
import sys

cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)

MyInt = __import__("100-my_int").MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
