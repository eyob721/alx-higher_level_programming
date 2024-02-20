#!/usr/bin/python3
"""Task 2"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

append_write = __import__("2-append_write").append_write

nb_characters_added = append_write(
    "file_append.txt", "This School is so cool!\n"
)
print(nb_characters_added)
