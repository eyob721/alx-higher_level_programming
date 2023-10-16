#!/usr/bin/python3
"""Test module for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class."""
    def setUp(self):
        # Create Square objects for normal test cases
        self.sqr1 = Square(5)
        self.sqr2 = Square(10, 3, 3, 7)

    def test_size_normal(self):
        """Test size of the square for normal cases"""
        self.assertEqual(self.sqr1.size, 5)
        self.assertEqual(self.sqr2.size, 10)

    def test_size_edges(self):
        """Test size of the square for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, "10")
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, 10.5)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, -1)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, 0)

        # Check that width attribute's error is raised first before `height`,
        # `x` or `y`
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Square, True, '10', '10')
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Square, -1, -1, -1)

    def test_x_normal(self):
        """Test x position of the square for normal cases"""
        self.assertEqual(self.sqr1.x, 0)
        self.assertEqual(self.sqr2.x, 3)

    def test_x_edges(self):
        """Test x position of the square for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 5, "10", 3)
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 5, 10.5, 3)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Square, 5, -1, 3)

        # Check that x attribute's error is raised first before `y`
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Square, 5, '10', '10')
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Square, 5, -1, -1)

    def test_y_normal(self):
        """Test y position of the square for normal cases"""
        self.assertEqual(self.sqr1.y, 0)
        self.assertEqual(self.sqr2.y, 3)

    def test_y_edges(self):
        """Test y position of the square for edge cases"""

        # Check for type errors
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Square, 5, 3, "10")
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Square, 5, 3, 10.5)

        # Check for value errors
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Square, 5, 3, -1)

    def test_square_area(self):
        """Test area of the square"""
        self.assertEqual(self.sqr1.area(), 25)
        self.assertEqual(self.sqr2.area(), 100)
        self.assertEqual(Square(40210).area(), 1_616_844_100)

    def test_square_str(self):
        """Test the string representation of the square (i.e. __str__())"""
        self.assertMultiLineEqual(Square(4, 2, 1, 44).__str__(),
                                  "[Square] (44) 2/1 - 4")

    def test_square_update_args(self):
        """Test the update method of the Square, with *args"""
        sqr = Square(10, 10, 10, 10)
        sqr.update(89)
        self.assertMultiLineEqual(sqr.__str__(),
                                  "[Square] (89) 10/10 - 10")
        sqr.update(89, 2)
        self.assertMultiLineEqual(sqr.__str__(),
                                  "[Square] (89) 10/10 - 2")
        sqr.update(89, 2, 3)
        self.assertMultiLineEqual(sqr.__str__(),
                                  "[Square] (89) 3/10 - 2")
        sqr.update(89, 2, 3, 4)
        self.assertMultiLineEqual(sqr.__str__(),
                                  "[Square] (89) 3/4 - 2")

        # Check for large number of arguments
        sqr.update(16, 5, 7, 10, 3, 21, 44, 71, 0)
        self.assertMultiLineEqual(sqr.__str__(),
                                  "[Square] (16) 7/10 - 5")

    def test_square_update_kwargs(self):
        """Test the update method of the Square, with **kwargs"""
        r = Square(10, 10, 10, 10)
        r.update(size=1)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (10) 10/10 - 1")
        r.update(size=5, y=3, x=2)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (10) 2/3 - 5")
        r.update(x=7, id=18)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (18) 7/3 - 5")

    def test_square_update_args_and_kwargs(self):
        """Test the update method of the Square, with *args and **kwargs"""
        r = Square(10, 10, 10, 10)
        r.update(20, size=7, x=3, y=9)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (20) 10/10 - 10")
        r.update(20, 5, 3, y=1, x=1)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Square] (20) 3/10 - 5")

    def test_square_dictionary(self):
        """Test the dictionary representation of the Square object"""
        r = Square(3, id=4)
        self.assertEqual(r.to_dictionary(),
                         {'size': 3, 'x': 0, 'y': 0, 'id': 4})
        r.update(x=7, y=3)
        self.assertEqual(r.to_dictionary(),
                         {'size': 3, 'x': 7, 'y': 3, 'id': 4})
