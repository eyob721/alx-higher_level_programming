#!/usr/bin/python3
"""Task 2"""


class MyList(list):
    """A class that inherits from the list built in class."""

    def print_sorted(self):
        """Prints the list object in sorted order."""
        print(sorted(self))
