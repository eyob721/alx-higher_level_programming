#!/usr/bin/python3
"""Task 13"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text to a file after each line containing a specific string"""
    with open(filename, "r+", encoding="utf-8") as file:
        lines_list = file.readlines()
        for i, line in enumerate(lines_list):
            if line.find(search_string) != -1:
                lines_list[i] = line + new_string
        file.truncate(0)
        file.seek(0)
        file.writelines(lines_list)
