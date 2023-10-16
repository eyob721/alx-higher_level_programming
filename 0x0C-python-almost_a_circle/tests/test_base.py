#!/usr/bin/python3
"""Test module for the Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """Tests for Base class."""

    def test_id(self):
        """Test value of id of Base Class"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_base_json_string(self):
        """Test for json string representation """
        json_string = Base.to_json_string([])
        self.assertEqual('[]', json_string)

        b = Base(24)
        json_string = Base.to_json_string([b.__dict__])
        self.assertEqual('[{"id": 24}]', json_string)
