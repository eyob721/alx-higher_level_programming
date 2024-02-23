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
