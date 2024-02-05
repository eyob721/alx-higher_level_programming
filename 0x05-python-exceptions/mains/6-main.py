#!/usr/bin/python3
"""Main script for task 6"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

raise_exception_msg = __import__("6-raise_exception_msg").raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
