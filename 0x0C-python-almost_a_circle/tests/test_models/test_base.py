#!/usr/bin/python3
"""Tests for the Base class"""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def test_object_type(self):
        """Check an object of Base class is of type Base Class"""
        b = Base()
        self.assertTrue(type(b) is Base)
