#!/usr/bin/python3
"""Task 6"""


def load_from_json_file(filename):
    """Returns a Python object from a JSON string stored in a file."""
    import json

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
