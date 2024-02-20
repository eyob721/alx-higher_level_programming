#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
    """Reads a file."""
    with open(filename, "r", encoding="utf-8") as file:
        print("{}".format(file.read()), end="")
