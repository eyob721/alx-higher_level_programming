#!/usr/bin/python3
"""A module for task 12."""


class MyInt(int):
    """My inverted definition of int."""
    def __eq__(self, other):
        return self.real != other.real

    def __ne__(self, other):
        return self.real == other.real
