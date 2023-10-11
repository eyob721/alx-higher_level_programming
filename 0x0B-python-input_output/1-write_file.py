#!/usr/bin/python3
"""A module for task 1."""


def write_file(filename="", text=""):
    """Writes `text` to file `filename`"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
