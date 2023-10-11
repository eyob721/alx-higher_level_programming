#!/usr/bin/python3
"""A module for task 5."""


def save_to_json_file(my_obj, filename):
    """Saves string representation of an object to a file."""
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
