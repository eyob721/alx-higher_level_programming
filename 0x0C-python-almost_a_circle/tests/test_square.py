#!/usr/bin/python3
"""Test module for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class."""
    def setUp(self):
        # Create Square objects for normal test cases
        self.sqr1 = Square(10, 2)
        self.sqr2 = Square(2, 10, 3, 3, 7)

    def test_width_normal(self):
        """Test width of square for normal cases"""
        self.assertEqual(self.sqr1.width, 10)
        self.assertEqual(self.sqr2.width, 2)

    def test_width_edges(self):
        """Test width of square for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, "10", 3)
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, 10.5, 3)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, -1, 3)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, 0, 3)

        # Check that width attribute's error is raised first before `height`,
        # `x` or `y`
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, True, '10', '10', '10')
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, -1, 0, -1, -1)

    def test_height_normal(self):
        """Test height of square for normal cases"""
        self.assertEqual(self.sqr1.height, 2)
        self.assertEqual(self.sqr2.height, 10)

    def test_height_edges(self):
        """Test height of square for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Square, 3, "10")
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Square, 3, 10.5)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Square, 3, -1)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Square, 3, 0)

        # Check that height attribute's error is raised first before `x` or `y`
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Square, 3, True, '10', '10')
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Square, 3, 0, -1, -1)

    def test_x_normal(self):
        """Test x position of square for normal cases"""
        self.assertEqual(self.sqr1.x, 0)
        self.assertEqual(self.sqr2.x, 3)

    def test_x_edges(self):
        """Test x position of square for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 5, 7, "10", 3)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 5, 7, 10.5, 3)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Square, 5, 7, -1, 3)

        # Check that x attribute's error is raised first before `y`
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 5, 7, '10', '10')
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Square, 5, 7, -1, -1)

    def test_y_normal(self):
        """Test y position of square for normal cases"""
        self.assertEqual(self.sqr1.y, 0)
        self.assertEqual(self.sqr2.y, 3)

    def test_y_edges(self):
        """Test y position of square for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Square, 5, 7, 3, "10")
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Square, 5, 7, 3, 10.5)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Square, 5, 7, 3, -1)

    def test_square_area(self):
        """Test area of square"""
        self.assertEqual(Square(3, 5).area(), 15)
        self.assertEqual(Square(41, 10).area(), 410)
        self.assertEqual(Square(40210, 350).area(), 14_073_500)

    def test_square_str(self):
        """Test the string representation of the square (i.e. __str__())"""
        self.assertMultiLineEqual(Square(4, 6, 2, 1, 44).__str__(),
                                  "[Square] (44) 2/1 - 4/6")
        self.assertMultiLineEqual(Square(10, 20).__str__(),
                                  "[Square] (12) 0/0 - 10/20")

    def test_square_update_args(self):
        """Test the update method of the Square, with *args"""
        r = Square(10, 10, 10, 10, 10)
        r.update(89)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (89) 4/5 - 2/3")
        # Check for large number of arguments
        r.update(16, 5, 7, 10, 3, 21, 44, 71, 0)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (16) 10/3 - 5/7")

    def test_square_update_kwargs(self):
        """Test the update method of the Square, with **kwargs"""
        r = Square(10, 10, 10, 10, 10)
        r.update(height=1)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (10) 10/10 - 10/1")
        r.update(width=5, y=3, x=2)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (10) 2/3 - 5/1")
        r.update(x=7, id=18)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (18) 7/3 - 5/1")

    def test_square_update_args_and_kwargs(self):
        """Test the update method of the Square, with *args and **kwargs"""
        r = Square(10, 10, 10, 10, 10)
        r.update(20, height=1, width=7, x=3, y=9)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (20) 10/10 - 10/10")
        r.update(20, 5, 3, y=1, x=1)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (20) 10/10 - 5/3")
