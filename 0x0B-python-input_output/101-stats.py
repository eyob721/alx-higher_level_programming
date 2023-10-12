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


def print_status():
    print(f"File size: {total_size:d}")
    for code in code_counts:
        if code_counts[code] != 0:
            print(f"{code}: {code_counts[code]:d}")


def is_correct_format(line):
    """Checks the format of a line."""


try:
    for line in sys.stdin:
        line_count += 1
        file_size = int(line.rsplit(' ', 1)[-1].rstrip(('\n')))
        code = line.rsplit(' ', 2)[-2]
        total_size += file_size
        code_counts[code] += 1
        if line_count % 10 == 0:
            print_status()
            line_count = 0
finally:
    if line_count == 0 or line_count % 10 != 0:
        print_status()
