#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

print_last_digit = __import__("9-print_last_digit").print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
