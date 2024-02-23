#!/usr/bin/python3
"""Tests for the Rectangle class"""
import unittest

from models.base import Base
from models.rectangle import Rectangle


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
        self.assertRaisesRegex(
            TypeError,
            r"^width must be an integer$",
            Rectangle,
            width="3",
            height=5,
        )
        self.assertRaisesRegex(
            TypeError,
            r"^width must be an integer$",
            Rectangle,
            width=[3],
            height=5,
        )
        self.assertRaisesRegex(
            TypeError,
            r"^width must be an integer$",
            Rectangle,
            width=(3,),
            height=5,
        )
        self.assertRaisesRegex(
            TypeError,
            r"^width must be an integer$",
            Rectangle,
            width={1: 3},
            height=5,
        )
        self.assertRaisesRegex(
            TypeError,
            r"^width must be an integer$",
            Rectangle,
            width=None,
            height=5,
        )

    def test_ValueError_exception_for_width(self):
        """Check raised exception and message when given wrong value

        Note:
            given value for width must be > 0

        """
        self.assertRaisesRegex(
            ValueError,
            r"^width must be > 0$",
            Rectangle,
            width=-7,
            height=5,
        )
        self.assertRaisesRegex(
            ValueError,
            r"^width must be > 0$",
            Rectangle,
            width=0,
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
        self.assertRaisesRegex(
            TypeError,
            r"^height must be an integer$",
            Rectangle,
            width=5,
            height="3",
        )
        self.assertRaisesRegex(
            TypeError,
            r"^height must be an integer$",
            Rectangle,
            width=5,
            height=[3],
        )
        self.assertRaisesRegex(
            TypeError,
            r"^height must be an integer$",
            Rectangle,
            width=5,
            height=(3,),
        )
        self.assertRaisesRegex(
            TypeError,
            r"^height must be an integer$",
            Rectangle,
            width=5,
            height={1: 3},
        )
        self.assertRaisesRegex(
            TypeError,
            r"^height must be an integer$",
            Rectangle,
            width=5,
            height=None,
        )

    def test_ValueError_exception_for_height(self):
        """Check raised exception and message when given wrong value

        Note:
            given value for height must be > 0

        """
        self.assertRaisesRegex(
            ValueError,
            r"^height must be > 0$",
            Rectangle,
            width=5,
            height=-7,
        )
        self.assertRaisesRegex(
            ValueError,
            r"^height must be > 0$",
            Rectangle,
            width=5,
            height=0,
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
