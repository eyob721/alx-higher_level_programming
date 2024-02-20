#!/usr/bin/python3
"""Task 13"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

append_after = __import__("100-append_after").append_after

append_after("mains/append_after_100.txt", "Python", '"C is fun!"\n')
