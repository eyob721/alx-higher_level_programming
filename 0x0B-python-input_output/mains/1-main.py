#!/usr/bin/python3
"""Task 1"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

write_file = __import__("1-write_file").write_file

nb_characters = write_file(
    "mains/my_first_file.txt", "This School is so cool!\n"
)
print(nb_characters)
