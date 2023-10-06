#!/usr/bin/python3
"""A module that contains unit tests for task 5.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([10.90, 15.01, 14.1]), 15.01)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([7, 7, 7, 7, 7]), 7)
        self.assertEqual(max_integer([-1, -10, -100]), -1)
        self.assertEqual(max_integer([1000000000000, 10]), 1000000000000)
        self.assertEqual(max_integer(), None)
