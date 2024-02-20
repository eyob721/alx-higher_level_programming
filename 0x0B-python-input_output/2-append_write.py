#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """Writes `text` to file `filename`"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
