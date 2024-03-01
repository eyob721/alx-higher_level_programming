#!/usr/bin/python3
"""Tests for the square class"""
import json
import os
import unittest
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle
from models.square import Square


def remove_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_square_object_type(self):
        """Check that square object it of type Square class"""
        s = Square(3)
        self.assertTrue(type(s) is Square)

    def test_square_class_inheritance(self):
        """Check that square object is a subclass of Rectangle class"""
        s = Square(3)
        # Check exact inheritance
        self.assertTrue(
            type(s) is not Rectangle and issubclass(type(s), Rectangle)
        )

    def test_square_has_rectangle_attributes(self):
        """Check that square object has Base class attributes"""
        s = Square(3)
        r = Rectangle(3, 5)
        for rectangle_attr in r.__dict__:
            self.assertTrue(rectangle_attr in s.__dict__)


class TestSquareWidth(unittest.TestCase):
    """Test cases for the Square - width attribute"""

    def test_width_exists(self):
        """Check that the Square class has the width attribute"""
        s = Square(3)
        self.assertTrue("width" in dir(s))

    def test_width_assigned_correct_value(self):
        """Check width is assigned the correct given value"""
        s = Square(3)
        self.assertEqual(s.width, 3)

    def test_width_is_equal_to_height(self):
        """Check width and height are equal"""
        s = Square(3)
        self.assertEqual(s.width, s.height)

    def test_width_assigned_value_type(self):
        """Check if the assigned value of width is of type int"""
        s = Square(3)
        self.assertTrue(type(s.width) is int)

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
                Square,
                size=it,
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
                Square,
                size=iv,
            )


class TestSquareHeight(unittest.TestCase):
    """Test cases for the Square - Height attribute"""

    def test_height_exists(self):
        """Check that the Square class has the height attribute"""
        s = Square(3)
        self.assertTrue("height" in dir(s))

    def test_height_assigned_correct_value(self):
        """Check height is assigned the correct given value"""
        s = Square(3)
        self.assertEqual(s.height, 3)

    def test_height_assigned_value_type(self):
        """Check if the assigned value of height is of type int"""
        s = Square(3)
        self.assertTrue(type(s.height) is int)

    def test_TypeError_exception_for_height(self):
        """Check raised exception and message when given wrong type of value

        Note:
            type of given value for height must be an integer

        """
        s = Square(3)
        invalid_types = [3.1, True, 1 + 2j, "3", [3], (7,), {"value": 3}]

        def set_height(value):
            s.height = value

        for it in invalid_types:
            self.assertRaisesRegex(
                TypeError,
                r"^height must be an integer$",
                set_height,
                it,
            )

    def test_ValueError_exception_for_height(self):
        """Check raised exception and message when given wrong value

        Note:
            given value for height must be > 0

        """
        s = Square(3)
        invalid_values = [-19, -7, 0]

        def set_height(value):
            s.height = value

        for iv in invalid_values:
            self.assertRaisesRegex(
                ValueError,
                r"^height must be > 0$",
                set_height,
                iv,
            )


class TestSquareX(unittest.TestCase):
    """Test cases for the Square - x attribute"""

    def test_x_exists(self):
        """Check that the Square class has the x attribute"""
        s = Square(3)
        self.assertTrue("x" in dir(s))

    def test_x_assigned_correct_value(self):
        """Check x is assigned the correct given value"""
        s = Square(3)
        self.assertEqual(s.x, 0)

        s = Square(3, 2, 10)
        self.assertEqual(s.x, 2)

    def test_x_assigned_value_type(self):
        """Check if the assigned value of x is of type int"""
        s = Square(3)
        self.assertTrue(type(s.x) is int)

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
                Square,
                size=3,
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
            Square,
            size=5,
            x=-2,
            y=10,
        )


class TestSquareY(unittest.TestCase):
    """Test cases for the Square - y attribute"""

    def test_y_exists(self):
        """Check that the Square class has the y attribute"""
        s = Square(3)
        self.assertTrue("y" in dir(s))

    def test_y_assigned_correct_value(self):
        """Check y is assigned the correct given value"""
        s = Square(3)
        self.assertEqual(s.y, 0)

        s = Square(3, 2, 10)
        self.assertEqual(s.y, 10)

    def test_y_assigned_value_type(self):
        """Check if the assigned value of y is of type int"""
        s = Square(3)
        self.assertTrue(type(s.y) is int)

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
                Square,
                size=3,
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
            Square,
            size=5,
            x=10,
            y=-2,
        )


class TestSquareArea(unittest.TestCase):
    """Test cases for the Square - area method"""

    def test_area_exists(self):
        """Check that the area method is defined"""
        s = Square(3)
        self.assertTrue("area" in dir(s))

    def test_area_value(self):
        """Check area method returns correct value"""
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_area_value_type(self):
        """Check area method returns an int"""
        s = Square(3)
        self.assertIs(type(s.area()), int)


class TestSquareDisplay(unittest.TestCase):
    """Test cases for the Square - display method"""

    def test_display_exists(self):
        """Check that the display method is defined"""
        s = Square(3)
        self.assertTrue("display" in dir(s))

    def test_display_output(self):
        """Check the output of the display method"""
        values = [(3,), (2, 20, 10), (1, 0, 40), (3, 4, 2, 12)]
        for v in values:
            s = Square(*v)
            exp_output = ("\n" * s.y) + (
                (" " * s.x + "#" * s.width + "\n") * s.height
            )
            with patch("sys.stdout", new=StringIO()) as got_output:
                s.display()
                self.assertEqual(got_output.getvalue(), exp_output)


class TestSquareStr(unittest.TestCase):
    """Test cases for the Square - __str__ method"""

    def test_str_return_type(self):
        """Check that __str__ returns a string"""
        s = Square(3)
        self.assertTrue(type(s.__str__()) is str)

    def test_str_return_value(self):
        """Check __str__ returns the correct value"""
        values = [(3,), (1, 10, 15), (3, 4, 2, 12)]
        for v in values:
            s = Square(*v)
            exp_output = "[Square] ({}) {}/{} - {}".format(
                s.id, s.x, s.y, s.size
            )
            got_output = s.__str__()
            self.assertEqual(got_output, exp_output)


class TestSquareSize(unittest.TestCase):
    """Test cases for the Square - size attribute"""

    def test_size_exists(self):
        """Check that the Square class has the size attribute"""
        s = Square(3)
        self.assertTrue("size" in dir(s))

    def test_size_assigned_correct_value(self):
        """Check size is assigned the correct given value"""
        s = Square(3)
        self.assertEqual(s.size, 3)

        s.size = 7
        self.assertEqual(s.size, 7)

    def test_width_and_height_are_the_same(self):
        """Check that width and height have the same value"""
        s = Square(3)
        self.assertEqual(s.width, s.height)

        s.size = 10
        self.assertEqual(s.width, s.height)

    def test_size_assigned_value_type(self):
        """Check if the assigned value of size is of type int"""
        s = Square(3)
        self.assertTrue(type(s.size) is int)

    def test_TypeError_exception_for_size(self):
        """Check raised exception and message when given wrong type of value

        Note:
            type of given value for size must be an integer

        """
        invalid_types = [3.1, True, 1 + 2j, "3", [3], (7,), {"value": 3}]

        for it in invalid_types:
            self.assertRaisesRegex(
                TypeError,
                r"^width must be an integer$",
                Square,
                size=it,
            )

        s = Square(3)

        def set_size(value):
            s.size = value

        for it in invalid_types:
            self.assertRaisesRegex(
                TypeError,
                r"^width must be an integer$",
                set_size,
                it,
            )

    def test_ValueError_exception_for_size(self):
        """Check raised exception and message when given wrong value

        Note:
            given value for size must be > 0

        """
        invalid_values = [-19, -7, 0]
        for iv in invalid_values:
            self.assertRaisesRegex(
                ValueError,
                r"^width must be > 0$",
                Square,
                size=iv,
            )

        s = Square(3)

        def set_size(value):
            s.size = value

        for iv in invalid_values:
            self.assertRaisesRegex(
                ValueError,
                r"^width must be > 0$",
                set_size,
                iv,
            )


class TestSquareUpdate(unittest.TestCase):
    """Test cases for the Square - update method"""

    def test_update_exists(self):
        """Check that the update method is defined"""
        s = Square(3)
        self.assertTrue("update" in dir(s))

    def test_attributes_are_updated_correctly_using_args(self):
        """Check if the attributes are updated correctly using args"""
        s = Square(3)

        exp_output = s.__str__()
        s.update()
        self.assertEqual(s.__str__(), exp_output)

        s.update(89)
        exp_output = "[Square] (89) 0/0 - 3"
        self.assertEqual(s.__str__(), exp_output)

        s.update(89, 2)
        exp_output = "[Square] (89) 0/0 - 2"
        self.assertEqual(s.__str__(), exp_output)

        s.update(89, 2, 3)
        exp_output = "[Square] (89) 3/0 - 2"
        self.assertEqual(s.__str__(), exp_output)

        s.update(89, 2, 3, 4)
        exp_output = "[Square] (89) 3/4 - 2"
        self.assertEqual(s.__str__(), exp_output)

        s.update(89, 2, 3, 4, 5)
        exp_output = "[Square] (89) 3/4 - 2"
        self.assertEqual(s.__str__(), exp_output)

    def test_attributes_are_updated_correctly_using_kwargs(self):
        """Check if the attributes are updated correctly using kwargs"""
        s = Square(3)

        test_values = {"id": 89, "size": 16, "x": 12, "y": 19}

        for key, value in test_values.items():
            s.update(**{key: value})
            self.assertEqual(getattr(s, key), value)

    def test_unknown_attributes_are_not_set_using_kwargs(self):
        """Check that unknown attributes are not set using kwargs"""
        s = Square(3)

        unknown_attributes = {"test": 89, "sample": 16, "unknown": 29}

        for key, value in unknown_attributes.items():
            s.update(**{key: value})
            self.assertTrue(key not in dir(s))


class TestSquareToDictionary(unittest.TestCase):
    """Test cases for the Square - to_dictionary method"""

    def test_to_dictionary_exists(self):
        """Check that the method to_dictionary is defined"""
        s = Square(3)
        self.assertTrue("to_dictionary" in dir(s))

    def test_to_dictionary_returned_a_dictionary(self):
        """Check that a dictionary is returned"""
        s = Square(3)
        self.assertTrue(type(s.to_dictionary()) is dict)

    def test_to_dictionary_returned_correct_value(self):
        s = Square(3, 0, 0, 12)
        got = s.to_dictionary()

        self.assertEqual(got["id"], 12)
        self.assertEqual(got["size"], 3)
        self.assertEqual(got["x"], 0)
        self.assertEqual(got["y"], 0)

        s.x = 10
        s.y = 7
        got = s.to_dictionary()
        self.assertEqual(got["x"], 10)
        self.assertEqual(got["y"], 7)


class TestSquareToJsonString(unittest.TestCase):
    """Test cases for the Square - to_json_string method"""

    def test_to_json_string_method_exists(self):
        """Check that the method is defined"""
        s = Square(3)
        self.assertTrue("to_json_string" in dir(s))

    def test_to_json_string_returned_value(self):
        """Check returned value is correct"""
        s = Square(3)

        # None
        self.assertEqual("[]", s.to_json_string(None))

        # empty list
        self.assertEqual("[]", s.to_json_string([]))

        # list of dictionaries
        self.assertEqual(
            json.dumps([s.to_dictionary()]),
            s.to_json_string([s.to_dictionary()]),
        )


class TestSquareFromJsonString(unittest.TestCase):
    """Test cases for the Square - from_json_string method"""

    def test_from_json_string_method_exists(self):
        """Check that the method is defined"""
        s = Square(3)
        self.assertTrue("from_json_string" in dir(s))

    def test_from_json_string_returned_value(self):
        """Check returned value is correct"""
        s = Square(3)

        # None
        self.assertEqual([], s.from_json_string(None))

        # empty list
        self.assertEqual([], s.from_json_string([]))

        # list of dictionaries
        self.assertEqual(
            [s.to_dictionary()],
            s.from_json_string(json.dumps([s.to_dictionary()])),
        )


class TestSquareSaveToFile(unittest.TestCase):
    """Test cases for the Square - save_to_file method"""

    def test_save_to_file_method_exists(self):
        """Check save_to_file method is defined"""
        s = Square(3)
        self.assertTrue("save_to_file" in dir(s))

    def test_save_to_file_method_file_contents(self):
        """Check save_to_file method correctly saves the file"""
        s = Square(3)

        # None
        s.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Square.json")

        # []
        s.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Square.json")

        # (1, 2, 3)
        s.save_to_file((1, 2, 3))
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read().rstrip("\n"))
        remove_file("Square.json")

        # list of Square objects
        list_objs = [Square(2), Square(1, 3, 5), Square(5, 10, 2, 3)]
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        exp_json_string = json.dumps(list_dicts)
        s.save_to_file(list_objs)
        with open("Square.json", "r") as file:
            self.assertEqual(exp_json_string, file.read().rstrip("\n"))
        remove_file("Square.json")


class TestSquareLoadFromFile(unittest.TestCase):
    """Test cases for the Square - load_from_file method"""

    def test_load_from_file_method_exists(self):
        """Check load_from_file method is defined"""
        s = Square(3)
        self.assertTrue("load_from_file" in dir(s))

    def test_load_from_file_method_file_contents(self):
        """Check load_from_file method correctly loads the file"""
        s1 = Square(3)
        s2 = Square(7)
        s3 = Square(10)

        # File doesn't exist
        remove_file("Square.json")
        self.assertEqual([], Square.load_from_file())

        # File exists (what is saved must equal what is loaded)
        list_objs = [s1, s2, s3]
        list_dicts = [r.to_dictionary() for r in list_objs]
        Square.save_to_file(list_objs)

        list_objs_loaded = Square.load_from_file()
        for obj in list_objs_loaded:
            self.assertTrue(type(obj) is Square)
        list_dicts_loaded = [r.to_dictionary() for r in list_objs_loaded]
        self.assertEqual(list_dicts, list_dicts_loaded)
        remove_file("Square.json")


class TestSquareCreate(unittest.TestCase):
    """Test cases for the Square - create method"""

    def test_create_method_exists(self):
        """Check that the create method is defined"""
        s = Square(3)
        self.assertTrue("create" in dir(s))

    def test_create_method_returns_correct_value(self):
        """Check that the create method returns the correct value"""
        s1 = Square(3)
        s1_dict = s1.to_dictionary()

        s2 = s1.create(**s1_dict)
        self.assertTrue(type(s2) is Square)

        s2_dict = s2.to_dictionary()
        self.assertTrue(s1_dict == s2_dict)


class TestSquareFileCSV(unittest.TestCase):
    """Test cases for the Square - save_to_file_csv and load_from_file_csv"""

    def test_save_to_file_csv_method_exists(self):
        """Check save_to_file_csv method is defined"""
        s = Square(3)
        self.assertTrue("save_to_file_csv" in dir(s))

    def test_load_from_file_csv_method_exists(self):
        """Check load_from_file_csv method is defined"""
        s = Square(3)
        self.assertTrue("load_from_file_csv" in dir(s))

    def test_save_and_load_to_and_from_a_csv_file(self):
        """Check saving and loading from a csv file"""
        s = Square(3)

        # None
        s.save_to_file_csv(None)
        with open("Square.csv", "r") as file:
            self.assertEqual("", file.read().rstrip("\n"))
        remove_file("Square.csv")

        # []
        s.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            self.assertEqual("", file.read().rstrip("\n"))
        remove_file("Square.csv")

        # (1, 2, 3)
        s.save_to_file_csv((1, 2, 3))
        with open("Square.csv", "r") as file:
            self.assertEqual("", file.read().rstrip("\n"))
        remove_file("Square.csv")

        # Load a file that doesn't exist
        remove_file("Square.csv")
        self.assertEqual([], Square.load_from_file_csv())

        # Load a file that exists (what is saved must equal what is loaded)
        s1 = Square(3)
        s2 = Square(7)
        s3 = Square(10)

        list_objs = [s1, s2, s3]
        list_dicts = [r.to_dictionary() for r in list_objs]
        Square.save_to_file_csv(list_objs)

        list_objs_loaded = Square.load_from_file_csv()
        for obj in list_objs_loaded:
            self.assertTrue(type(obj) is Square)
        list_dicts_loaded = [r.to_dictionary() for r in list_objs_loaded]
        self.assertEqual(list_dicts, list_dicts_loaded)
        remove_file("Square.csv")
