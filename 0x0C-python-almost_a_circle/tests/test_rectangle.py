#!/usr/bin/python3
"""Test module for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""

    def test_id(self):
        """Test for id of Rectangles
        Note:
            Previous Base class test has set the value of `__nb_objects` to 4.
            So new objects of Rectangle class will have ids starting from 5,
            if id is None.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)

        r2 = Rectangle(2, 10, 1, 1, 7)
        self.assertEqual(r2.id, 7)
