#!/usr/bin/python3
"""A module that contains unit tests for task 5.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test class for the function `max_integer`."""

    def test_normal_cases(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
