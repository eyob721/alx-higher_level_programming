#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

fizzbuzz = __import__("12-fizzbuzz").fizzbuzz

fizzbuzz()
print("")
