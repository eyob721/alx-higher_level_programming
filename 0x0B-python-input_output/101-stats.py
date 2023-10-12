#!/usr/bin/python3
"""A module for task 14.

This module is a script for log parsing.

"""
import sys

code_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
line_count = 0
total_size = 0


def initialize_counts():
    """Intializes the status code counts to 0"""
    for code in code_counts:
        code_counts[code] = 0


def print_status():
    print(f"File size: {total_size:d}")
    for code in code_counts:
        print(f"{code:d}: {code_counts[code]:d}")


for line in sys.stdin:
    file_size = line.rsplit(' ', 1)[-1].rstrip(('\n'))
    code = line.rsplit(' ', 2)[-2]
    print("code: {} size: {}".format(code, file_size))
