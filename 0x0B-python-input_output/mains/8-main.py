#!/usr/bin/python3
"""Task 8"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

MyClass = __import__("8-my_class").MyClass
class_to_json = __import__("8-class_to_json").class_to_json

m = MyClass("John")
m.number = 89
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
