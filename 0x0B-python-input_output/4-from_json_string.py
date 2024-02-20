#!/usr/bin/python3
"""Task 4"""


def from_json_string(my_str):
    """Returns an object from a JSON string representation."""
    import json

    return json.loads(my_str)
