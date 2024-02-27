#!/usr/bin/python3
"""Tests for the square class"""
import unittest
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle
from models.square import Square


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
                s.id, s.x, s.y, s.width
            )
            got_output = s.__str__()
            self.assertEqual(got_output, exp_output)
