#!/usr/bin/python3
"""Task 1 main script"""
import os
import sys

cur_dir = os.path.dirname(os.path.realpath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)

lookup = __import__("0-lookup").lookup


class MyClass1(object):
    """Doc"""

    pass


class MyClass2(object):
    """Doc"""

    my_attr1 = 3

    def my_meth(self):
        """Doc"""
        pass


print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
