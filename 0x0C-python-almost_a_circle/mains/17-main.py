#!/usr/bin/python3
"""Task 17"""
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from models.rectangle import Rectangle  # noqa

if __name__ == "__main__":

    list_input = [
        {"id": 89, "width": 10, "height": 4},
        {"id": 7, "width": 1, "height": 7},
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))
