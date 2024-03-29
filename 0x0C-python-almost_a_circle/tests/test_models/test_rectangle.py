#!/usr/bin/python3
"""Tests for the Rectangle class"""
import json
import os
import unittest
from io import StringIO
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle


def remove_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_rectangle_object_type(self):
        """Check that rectangle object it of type Rectangle class"""
        r = Rectangle(3, 5)
        self.assertTrue(type(r) is Rectangle)

    def test_rectangle_class_inheritance(self):
        """Check that rectangle object is a subclass of Base class"""
        r = Rectangle(3, 5)
        # Check exact inheritance
        self.assertTrue(type(r) is not Base and issubclass(type(r), Base))

    def test_rectangle_has_base_attributes(self):
        """Check that rectangle object has Base class attributes"""
        r = Rectangle(3, 5)
        b = Base()
        for base_attr in b.__dict__:
            self.assertTrue(base_attr in r.__dict__)


class TestRectangleId(unittest.TestCase):
    """Test cases for the Rectangle - id attribute"""

    def test_id_exists(self):
        """Check that the Rectangle class has the id attribute"""
        r = Rectangle(3, 5)
        self.assertTrue("id" in dir(r))

    def test_id_assigned_correct_value(self):
        """Check id is assigned the correct given value"""

        r = Rectangle(3, 5)
        self.assertEqual(r.id, getattr(r, "_Base__nb_objects"))

        r = Rectangle(3, 5, 2, 10, 21)
        self.assertEqual(r.id, 21)


class TestRectangleWidth(unittest.TestCase):
    """Test cases for the Rectangle - width attribute"""

    def test_width_exists(self):
        """Check that the Rectangle class has the width attribute"""
        r = Rectangle(3, 5)
        self.assertTrue("width" in dir(r))
        self.assertTrue("_Rectangle__width" in dir(r))

    def test_width_assigned_correct_value(self):
        """Check width is assigned the correct given value"""
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)

    def test_width_assigned_value_type(self):
        """Check if the assigned value of width is of type int"""
        r = Rectangle(3, 5)
        self.assertTrue(type(r.width) is int)

    def test_TypeError_exception_for_width(self):
        """Check raised exception and message when given wrong type of value

        Note:
            type of given value for width must be an integer

        """
        invalid_types = [3.1, True, 1 + 2j, "3", [3], (7,), {"value": 3}]
        for it in invalid_types:
            self.assertRaisesRegex(
                TypeError,
                r"^width must be an integer$",
                Rectangle,
                width=it,
                height=5,
            )

    def test_ValueError_exception_for_width(self):
        """Check raised exception and message when given wrong value

        Note:
            given value for width must be > 0

        """
        invalid_values = [-19, -7, 0]
        for iv in invalid_values:
            self.assertRaisesRegex(
                ValueError,
                r"^width must be > 0$",
                Rectangle,
                width=iv,
                height=5,
            )


class TestRectangleHeight(unittest.TestCase):
    """Test cases for the Rectangle - height attribute"""

    def test_height_exists(self):
        """Check that the Rectangle class has the height attribute"""
        r = Rectangle(3, 5)
        self.assertTrue("height" in dir(r))
        self.assertTrue("_Rectangle__height" in dir(r))

    def test_height_assigned_correct_value(self):
        """Check height is assigned the correct given value"""
        r = Rectangle(3, 5)
        self.assertEqual(r.height, 5)

    def test_height_assigned_value_type(self):
        """Check if the assigned value of height is of type int"""
        r = Rectangle(3, 5)
        self.assertTrue(type(r.height) is int)

    def test_TypeError_exception_for_height(self):
        """Check raised exception and message when given wrong type of value

        Note:
            type of given value for height must be an integer

        """
        invalid_types = [3.1, True, 1 + 2j, "3", [3], (7,), {"value": 3}]
        for it in invalid_types:
            self.assertRaisesRegex(
                TypeError,
                r"^height must be an integer$",
                Rectangle,
                width=5,
                height=it,
            )

    def test_ValueError_exception_for_height(self):
        """Check raised exception and message when given wrong value

        Note:
            given value for height must be > 0

        """
        invalid_values = [-19, -7, 0]
        for iv in invalid_values:
            self.assertRaisesRegex(
                ValueError,
                r"^height must be > 0$",
                Rectangle,
                width=5,
                height=iv,
            )


class TestRectangleX(unittest.TestCase):
    """Test cases for the Rectangle - x attribute"""

    def test_x_exists(self):
        """Check that the Rectangle class has the x attribute"""
        r = Rectangle(3, 5)
        self.assertTrue("x" in dir(r))
        self.assertTrue("_Rectangle__x" in dir(r))

    def test_x_assigned_correct_value(self):
        """Check x is assigned the correct given value"""
        r = Rectangle(3, 5)
        self.assertEqual(r.x, 0)

        r = Rectangle(3, 5, 2, 10)
        self.assertEqual(r.x, 2)

    def test_x_assigned_value_type(self):
        """Check if the assigned value of x is of type int"""
        r = Rectangle(3, 5)
        self.assertTrue(type(r.x) is int)

    def test_TypeError_exception_for_x(self):
        """Check raised exception and message when given wrong type of value

        Note:
            type of given value for x must be an integer

        """
        invalid_types = [3.1, True, 1 + 2j, "3", [3], (7,), {"value": 3}]
        for it in invalid_types:
            self.assertRaisesRegex(
                TypeError,
                r"^x must be an integer$",
                Rectangle,
                width=3,
                height=5,
                x=it,
                y=10,
            )

    def test_ValueError_exception_for_x(self):
        """Check raised exception and message when given wrong value

        Note:
            given value for x must be >= 0

        """
        self.assertRaisesRegex(
            ValueError,
            r"^x must be >= 0$",
            Rectangle,
            width=5,
            height=7,
            x=-2,
            y=10,
        )


class TestRectangleY(unittest.TestCase):
    """Test cases for the Rectangle - y attribute"""

    def test_y_exists(self):
        """Check that the Rectangle class has the y attribute"""
        r = Rectangle(3, 5)
        self.assertTrue("y" in dir(r))
        self.assertTrue("_Rectangle__y" in dir(r))

    def test_y_assigned_correct_value(self):
        """Check y is assigned the correct given value"""
        r = Rectangle(3, 5)
        self.assertEqual(r.y, 0)

        r = Rectangle(3, 5, 2, 10)
        self.assertEqual(r.y, 10)

    #
    def test_y_assigned_value_type(self):
        """Check if the assigned value of y is of type int"""
        r = Rectangle(3, 5)
        self.assertTrue(type(r.y) is int)

    def test_TypeError_exception_for_y(self):
        """Check raised exception and message when given wrong type of value

        Note:
            type of given value for y must be an integer

        """
        invalid_types = [3.1, True, 1 + 2j, "3", [3], (7,), {"value": 3}]
        for it in invalid_types:
            self.assertRaisesRegex(
                TypeError,
                r"^y must be an integer$",
                Rectangle,
                width=3,
                height=5,
                x=7,
                y=it,
            )

    def test_ValueError_exception_for_y(self):
        """Check raised exception and message when given wrong value

        Note:
            given value for y must be >= 0

        """
        self.assertRaisesRegex(
            ValueError,
            r"^y must be >= 0$",
            Rectangle,
            width=5,
            height=7,
            x=10,
            y=-2,
        )


class TestRectangleArea(unittest.TestCase):
    """Test cases for the Rectangle - area method"""

    def test_area_exists(self):
        """Check that the area method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("area" in dir(r))

    def test_area_value(self):
        """Check area method returns correct value"""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

        r.width = 29
        r.height = 44
        self.assertEqual(r.area(), 29 * 44)

        r = Rectangle(3, 7, 0, 0, 12)
        self.assertEqual(r.area(), 21)

    def test_area_value_type(self):
        """Check area method returns an int"""
        r = Rectangle(3, 5)
        self.assertIs(type(r.area()), int)


class TestRectangleDisplay(unittest.TestCase):
    """Test cases for the Rectangle - display method"""

    def test_display_exists(self):
        """Check that the display method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("display" in dir(r))

    def test_display_output(self):
        """Check the output of the display method"""
        values = [(3, 5), (2, 7, 20, 10), (1, 1, 0, 40), (3, 10, 4, 2, 12)]
        for v in values:
            r = Rectangle(*v)
            exp_output = ("\n" * r.y) + (
                (" " * r.x + "#" * r.width + "\n") * r.height
            )
            with patch("sys.stdout", new=StringIO()) as got_output:
                r.display()
                self.assertEqual(got_output.getvalue(), exp_output)


class TestRectangleStr(unittest.TestCase):
    """Test cases for the Rectangle - __str__ method"""

    def test_str_return_type(self):
        """Check that __str__ returns a string"""
        r = Rectangle(3, 5)
        self.assertTrue(type(r.__str__()) is str)

    def test_str_return_value(self):
        """Check __str__ returns the correct value"""
        values = [(3, 5), (2, 7), (1, 1), (3, 10, 4, 2, 12)]
        for v in values:
            r = Rectangle(*v)
            exp_output = "[Rectangle] ({}) {}/{} - {}/{}".format(
                r.id, r.x, r.y, r.width, r.height
            )
            got_output = r.__str__()
            self.assertEqual(got_output, exp_output)


class TestRectangleUpdate(unittest.TestCase):
    """Test cases for the Rectangle - update method"""

    def test_update_exists(self):
        """Check that the update method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("update" in dir(r))

    def test_attributes_are_updated_correctly_using_args(self):
        """Check if the attributes are updated correctly using args"""
        r = Rectangle(3, 5)

        exp_output = r.__str__()
        r.update()
        self.assertEqual(r.__str__(), exp_output)

        r.update(89)
        exp_output = "[Rectangle] (89) 0/0 - 3/5"
        self.assertEqual(r.__str__(), exp_output)

        r.update(89, 2)
        exp_output = "[Rectangle] (89) 0/0 - 2/5"
        self.assertEqual(r.__str__(), exp_output)

        r.update(89, 2, 3)
        exp_output = "[Rectangle] (89) 0/0 - 2/3"
        self.assertEqual(r.__str__(), exp_output)

        r.update(89, 2, 3, 4)
        exp_output = "[Rectangle] (89) 4/0 - 2/3"
        self.assertEqual(r.__str__(), exp_output)

        r.update(89, 2, 3, 4, 5)
        exp_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(r.__str__(), exp_output)

        r.update(89, 2, 3, 4, 5, 6)
        exp_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(r.__str__(), exp_output)

    def test_attributes_are_updated_correctly_using_kwargs(self):
        """Check if the attributes are updated correctly using kwargs"""
        r = Rectangle(3, 5)

        test_values = {"id": 89, "width": 16, "height": 29, "x": 12, "y": 19}

        for key, value in test_values.items():
            r.update(**{key: value})
            self.assertEqual(getattr(r, key), value)

    def test_unknown_attributes_are_not_set_using_kwargs(self):
        """Check that unknown attributes are not set using kwargs"""
        r = Rectangle(3, 5)

        unknown_attributes = {"test": 89, "sample": 16, "unknown": 29}

        for key, value in unknown_attributes.items():
            r.update(**{key: value})
            self.assertTrue(key not in dir(r))


class TestRectangleToDictionary(unittest.TestCase):
    """Test cases for the Rectangle - to_dictionary method"""

    def test_to_dictionary_exists(self):
        """Check that the method to_dictionary is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("to_dictionary" in dir(r))

    def test_to_dictionary_returned_a_dictionary(self):
        """Check that a dictionary is returned"""
        r = Rectangle(3, 5)
        self.assertTrue(type(r.to_dictionary()) is dict)

    def test_to_dictionary_returned_correct_value(self):
        r = Rectangle(3, 5, 0, 0, 12)
        got = r.to_dictionary()

        self.assertEqual(got["id"], 12)
        self.assertEqual(got["width"], 3)
        self.assertEqual(got["height"], 5)
        self.assertEqual(got["x"], 0)
        self.assertEqual(got["y"], 0)

        r.x = 10
        r.y = 7
        got = r.to_dictionary()
        self.assertEqual(got["x"], 10)
        self.assertEqual(got["y"], 7)


class TestRectangleToJsonString(unittest.TestCase):
    """Test cases for the Rectangle - to_json_string method"""

    def test_to_json_string_method_exists(self):
        """Check that the method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("to_json_string" in dir(r))

    def test_to_json_string_returned_value(self):
        """Check returned value is correct"""
        r = Rectangle(3, 5)

        # None
        self.assertEqual("[]", r.to_json_string(None))

        # empty list
        self.assertEqual("[]", r.to_json_string([]))

        # list of dictionaries
        self.assertEqual(
            json.dumps([r.to_dictionary()]),
            r.to_json_string([r.to_dictionary()]),
        )


class TestRectangleFromJsonString(unittest.TestCase):
    """Test cases for the Rectangle - from_json_string method"""

    def test_from_json_string_method_exists(self):
        """Check that the method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("from_json_string" in dir(r))

    def test_from_json_string_returned_value(self):
        """Check returned value is correct"""
        r = Rectangle(3, 5)

        # None
        self.assertEqual([], r.from_json_string(None))

        # empty list
        self.assertEqual([], r.from_json_string([]))

        # list of dictionaries
        self.assertEqual(
            [r.to_dictionary()],
            r.from_json_string(json.dumps([r.to_dictionary()])),
        )


class TestRectangleSaveToFile(unittest.TestCase):
    """Test cases for the Rectangle - save_to_file method"""

    def test_save_to_file_method_exists(self):
        """Check save_to_file method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("save_to_file" in dir(r))

    def test_save_to_file_method_file_contents(self):
        """Check save_to_file method correctly saves the file"""
        r = Rectangle(3, 5)

        # None
        r.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Rectangle.json")

        # []
        r.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Rectangle.json")

        # (1, 2, 3)
        r.save_to_file((1, 2, 3))
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Rectangle.json")

        # list of Rectangle objects
        list_objs = [Rectangle(2, 7), Rectangle(1, 10), Rectangle(5, 10, 2, 3)]
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        exp_json_string = json.dumps(list_dicts)
        r.save_to_file(list_objs)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(exp_json_string, file.read().rstrip("\n"))
        remove_file("Rectangle.json")


class TestRectangleLoadFromFile(unittest.TestCase):
    """Test cases for the Rectangle - load_from_file method"""

    def test_load_from_file_method_exists(self):
        """Check load_from_file method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("load_from_file" in dir(r))

    def test_load_from_file_method_file_contents(self):
        """Check load_from_file method correctly loads the file"""
        r1 = Rectangle(3, 5)
        r2 = Rectangle(7, 10)
        r3 = Rectangle(16, 21)

        # File doesn't exist
        remove_file("Rectangle.json")
        self.assertEqual([], Rectangle.load_from_file())

        # File exists (what is saved must equal what is loaded)
        list_objs = [r1, r2, r3]
        list_dicts = [r.to_dictionary() for r in list_objs]
        Rectangle.save_to_file(list_objs)

        list_objs_loaded = Rectangle.load_from_file()
        for obj in list_objs_loaded:
            self.assertTrue(type(obj) is Rectangle)
        list_dicts_loaded = [r.to_dictionary() for r in list_objs_loaded]
        self.assertEqual(list_dicts, list_dicts_loaded)
        remove_file("Rectangle.json")


class TestRectangleCreate(unittest.TestCase):
    """Test cases for the Rectangle - create method"""

    def test_create_method_exists(self):
        """Check that the create method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("create" in dir(r))

    def test_create_method_returns_correct_value(self):
        """Check that the create method returns the correct value"""
        r1 = Rectangle(3, 5)
        r1_dict = r1.to_dictionary()

        r2 = r1.create(**r1_dict)
        self.assertTrue(type(r2) is Rectangle)

        r2_dict = r2.to_dictionary()
        self.assertTrue(r1_dict == r2_dict)


class TestRectangleFileCSV(unittest.TestCase):
    """Test cases for Rectangle - save_to_file_csv and load_from_file_csv"""

    def test_save_to_file_csv_method_exists(self):
        """Check save_to_file_csv method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("save_to_file_csv" in dir(r))

    def test_load_from_file_csv_method_exists(self):
        """Check load_from_file_csv method is defined"""
        r = Rectangle(3, 5)
        self.assertTrue("load_from_file_csv" in dir(r))

    def test_save_and_load_to_and_from_a_csv_file(self):
        """Check saving and loading from a csv file"""
        r = Rectangle(3, 5)

        # None
        r.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual("", file.read().rstrip("\n"))
        remove_file("Rectangle.csv")

        # []
        r.save_to_file_csv([])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual("", file.read().rstrip("\n"))
        remove_file("Rectangle.csv")

        # (1, 2, 3)
        r.save_to_file_csv((1, 2, 3))
        with open("Rectangle.csv", "r") as file:
            self.assertEqual("", file.read().rstrip("\n"))
        remove_file("Rectangle.csv")

        # Load a file that doesn't exist
        remove_file("Rectangle.csv")
        self.assertEqual([], Rectangle.load_from_file_csv())

        # Load a file that exists (what is saved must equal what is loaded)
        r1 = Rectangle(3, 5)
        r2 = Rectangle(7, 10)
        r3 = Rectangle(16, 21)

        list_objs = [r1, r2, r3]
        list_dicts = [r.to_dictionary() for r in list_objs]
        Rectangle.save_to_file_csv(list_objs)

        list_objs_loaded = Rectangle.load_from_file_csv()
        for obj in list_objs_loaded:
            self.assertTrue(type(obj) is Rectangle)
        list_dicts_loaded = [r.to_dictionary() for r in list_objs_loaded]
        self.assertEqual(list_dicts, list_dicts_loaded)
        remove_file("Rectangle.csv")
