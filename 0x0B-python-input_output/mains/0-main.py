#!/usr/bin/python3
"""Task 0"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

read_file = __import__("0-read_file").read_file

read_file("mains/my_file_0.txt")
