#!/usr/bin/python3
"""Task 4"""


def text_indentation(text):
    """Prints a text with 2 new lines after each `.`, `?` and `:`

    Args:
        text (str): a given text

    Returns:
        None

    Raises:
        TypeError: if `text` is not a string

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.',
                        '.\n\n').replace(':', ':\n\n').replace('?', '?\n\n')
    lines = text.splitlines(keepends=True)
    for line in lines:
        print(line.strip(" \t"), end="")
