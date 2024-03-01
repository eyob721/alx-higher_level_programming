#!/usr/bin/python3
"""Tests for the Base class"""
import json
import os
import unittest

from models.base import Base


def remove_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


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


class TestBaseToJsonString(unittest.TestCase):
    """Test cases for the Base - to_json_string method"""

    def test_to_json_string_method_exists(self):
        """Check that the method is defined"""
        b = Base()
        self.assertTrue("to_json_string" in dir(b))

    def test_to_json_string_returned_value(self):
        """Check returned value is correct"""
        b = Base()

        # None
        self.assertEqual("[]", b.to_json_string(None))

        # empty list
        self.assertEqual("[]", b.to_json_string([]))

        sample_list = [
            {
                "colorList": ["Red", "Green", "Blue"],
                "carTuple": ("BMW", "Audi", "range rover"),
                "sampleString": "eyob721",
                "sampleInteger": 318,
                "sampleFloat": 3.14,
                "booleantrue": True,
                "booleanfalse": False,
                "nonevalue": None,
                "NanValue": float("NaN"),
            },
            {
                "name": "Eyob",
                "age": 29,
            },
            {
                "program": "Alx",
                "field": "Software Engineering",
            },
        ]

        # list of dictionaries
        self.assertEqual(
            json.dumps(sample_list), b.to_json_string(sample_list)
        )


class TestBaseSaveToFile(unittest.TestCase):
    """Test cases for the Base - save_to_file method"""

    def test_save_to_file_method_exists(self):
        """Check save_to_file method is defined"""
        b = Base()
        self.assertTrue("save_to_file" in dir(b))

    def test_save_to_file_method_file_contents(self):
        """Check save_to_file method correctly saves the file"""
        b = Base()

        # None
        b.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Base.json")

        # []
        b.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Base.json")

        # (1, 2, 3)
        b.save_to_file((1, 2, 3))
        with open("Base.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Base.json")


class TestBaseLoadFromFile(unittest.TestCase):
    """Test cases for the Base - load_from_file method"""

    def test_load_from_file_method_exists(self):
        """Check load_from_file method is defined"""
        b = Base()
        self.assertTrue("load_from_file" in dir(b))

    def test_load_from_file_method_file_contents(self):
        """Check load_from_file method correctly saves the file"""
        b = Base()

        # File doesn't exist
        remove_file("Base.json")
        self.assertEqual([], b.load_from_file())


class TestBaseFromJsonString(unittest.TestCase):
    """Test cases for the Base - from_json_string method"""

    def test_from_json_string_method_exists(self):
        """Check that the method is defined"""
        b = Base()
        self.assertTrue("from_json_string" in dir(b))

    def test_from_json_string_returned_value(self):
        """Check returned value is correct"""
        b = Base()

        # None
        self.assertEqual([], b.from_json_string(None))

        # empty list
        self.assertEqual([], b.from_json_string([]))

        sample_list = [
            {
                "colorList": ["Red", "Green", "Blue"],
                "sampleString": "eyob721",
                "sampleInteger": 318,
                "sampleFloat": 3.14,
                "booleantrue": True,
                "booleanfalse": False,
                "nonevalue": None,
            },
            {
                "name": "Eyob",
                "age": 29,
            },
            {
                "program": "Alx",
                "field": "Software Engineering",
            },
        ]
        sample_list_json = json.dumps(sample_list)

        # list of dictionaries
        self.assertEqual(sample_list, b.from_json_string(sample_list_json))


class TestBaseCreate(unittest.TestCase):
    """Test cases for the Base - create method"""

    def test_create_method_exists(self):
        """Check that the create method is defined"""
        b = Base()
        self.assertTrue("create" in dir(b))
