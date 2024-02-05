#!/usr/bin/python3
"""Main script for task 5"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

raise_exception = __import__("5-raise_exception").raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
