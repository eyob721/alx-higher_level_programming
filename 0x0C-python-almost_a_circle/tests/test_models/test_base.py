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

    def test_nb_objects_exists(self):
        """Check that __nb_objects exists"""
        self.assertTrue("_Base__nb_objects" in Base.__dict__)

    def test_nb_objects_type(self):
        """Check the __nb_objects type is an int"""
        self.assertTrue(type(Base.__dict__["_Base__nb_objects"]) is int)

    def test_nb_objects_value(self):
        """Check that __nb_objects is incremented only when id is None"""

        # When id value is given, __nb_objects must not be incremented
        nb_objects_first = Base.__dict__["_Base__nb_objects"]
        b = Base(3)
        nb_objects_second = Base.__dict__["_Base__nb_objects"]
        self.assertEqual(nb_objects_first, nb_objects_second)

        # When id value is not given, __nb_objects must be incremented
        b = Base()
        nb_objects_third = Base.__dict__["_Base__nb_objects"]
        self.assertEqual(nb_objects_third, nb_objects_second + 1)

    def test_id_exists(self):
        """Check that id exists"""
        b = Base()
        self.assertTrue("id" in b.__dict__)

    def test_id_type(self):
        """Check that type of id is an int"""
        b = Base()
        self.assertTrue(type(b.id) is int)

    def test_id_value(self):
        """Check the value of id"""

        # When id value is given, id must be equal with the given value
        b = Base(12)
        self.assertEqual(b.id, 12)

        # When no id is given, id must be equal with __nb_objects
        b = Base()
        nb_objects = getattr(b, "_Base__nb_objects")
        self.assertEqual(b.id, nb_objects)
