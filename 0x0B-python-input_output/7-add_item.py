#!/usr/bin/python3
"""Task 7

This script adds all its arguments to a list and then saves them to a json
file. If the json file has already a list in it, the new arguments are extended
to it.

"""
import json
from sys import argv

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

# Create the file if it doesn't exist
with open("add_item.json", "a", encoding="utf-8") as file:
    pass

# Load json object from the file
try:
    loaded_list = load_from_json_file("add_item.json")
except json.JSONDecodeError:
    loaded_list = []

# Add arguments to loaded list
loaded_list.extend(argv[1:])

# Save to json file
save_to_json_file(loaded_list, "add_item.json")
