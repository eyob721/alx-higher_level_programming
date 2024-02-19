#!/usr/bin/python3
"""Task 12"""


class MyInt(int):
    """My inverted definition of int."""

    def __eq__(self, other):
        """Inverted Equality"""
        return self.real != other.real

    def __ne__(self, other):
        """Inverted Inequality"""
        return self.real == other.real
