#!/usr/bin/python3
"""Test module for Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class."""
    def setUp(self):
        # Create Rectangle objects for normal test cases
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10, 3, 3, 7)

    def test_width_normal(self):
        """Test width of rectangle for normal cases"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)

    def test_width_edges(self):
        """Test width of rectangle for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, "10", 3)
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, 10.5, 3)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -1, 3)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, 0, 3)

        # Check that width attribute's error is raised first before `height`,
        # `x` or `y`
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, True, '10', '10', '10')
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -1, 0, -1, -1)

    def test_height_normal(self):
        """Test height of rectangle for normal cases"""
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)

    def test_height_edges(self):
        """Test height of rectangle for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 3, "10")
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 3, 10.5)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 3, -1)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 3, 0)

        # Check that height attribute's error is raised first before `x` or `y`
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 3, True, '10', '10')
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 3, 0, -1, -1)

    def test_x_normal(self):
        """Test x position of rectangle for normal cases"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 3)

    def test_x_edges(self):
        """Test x position of rectangle for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 5, 7, "10", 3)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 5, 7, 10.5, 3)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Rectangle, 5, 7, -1, 3)

        # Check that x attribute's error is raised first before `y`
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 5, 7, '10', '10')
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Rectangle, 5, 7, -1, -1)

    def test_y_normal(self):
        """Test y position of rectangle for normal cases"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 3)

    def test_y_edges(self):
        """Test y position of rectangle for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Rectangle, 5, 7, 3, "10")
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Rectangle, 5, 7, 3, 10.5)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Rectangle, 5, 7, 3, -1)

    def test_rectangle_area(self):
        """Test area of rectangle"""
        self.assertEqual(Rectangle(3, 5).area(), 15)
        self.assertEqual(Rectangle(41, 10).area(), 410)
        self.assertEqual(Rectangle(40210, 350).area(), 14_073_500)

    def test_rectangle_str(self):
        """Test the string representation of the rectangle (i.e. __str__())"""
        self.assertMultiLineEqual(Rectangle(4, 6, 2, 1, 44).__str__(),
                                  "[Rectangle] (44) 2/1 - 4/6")
        self.assertMultiLineEqual(Rectangle(10, 20).__str__(),
                                  "[Rectangle] (12) 0/0 - 10/20")
