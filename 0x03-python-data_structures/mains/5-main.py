#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

no_c = __import__("5-no_c").no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
print(no_c(""))
print(no_c(None))
