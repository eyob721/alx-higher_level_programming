#!/usr/bin/python3
"""Task 14

This module is a script for log parsing.

"""
import sys

code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}
line_count = 0
total_size = 0


def print_status():
    """Prints the status"""
    print(f"File size: {total_size:d}")
    for code in code_counts:
        if code_counts[code] != 0:
            print(f"{code}: {code_counts[code]:d}")


def get_file_size(line):
    """Checks the file size from the line."""
    try:
        file_size = int(line.rsplit(" ", 1)[-1].rstrip(("\n")))
    except Exception:
        return 0
    return file_size


def get_status_code(line):
    """Gets the status code"""
    try:
        code = line.rsplit(" ", 2)[-2]
    except Exception:
        return None
    if code not in code_counts:
        return None
    return code


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            line_count += 1
            file_size = get_file_size(line)
            total_size += file_size
            code = get_status_code(line)
            if code is not None:
                code_counts[code] += 1
            if line_count % 10 == 0:
                print_status()
    finally:
        if line_count == 0 or line_count % 10 != 0:
            print_status()
