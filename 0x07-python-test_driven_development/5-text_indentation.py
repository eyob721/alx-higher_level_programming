#!/usr/bin/python3
"""A module for task 4.

This module contains the function `text_indentation()`.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of the
    characters `.`, `?` and `:`

    Args:
        text (str): A given text.

    Returns:
        None

    Raises:
        TypeError: If `text` is not a string.

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.',
                        '.\n\n').replace(':', ':\n\n').replace('?', '?\n\n')
    lines = text.splitlines(keepends=True)
    for line in lines:
        print(line.strip(" \t"), end="")
