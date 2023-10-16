#!/usr/bin/python3
"""Test module for Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
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
        self.assertMultiLineEqual(Rectangle(10, 20, id=13).__str__(),
                                  "[Rectangle] (13) 0/0 - 10/20")

    def test_rectangle_display(self):
        """Test the rectangle display method"""
        rec = Rectangle(3, 5)
        with patch('sys.stdout', new=StringIO()) as output:
            expected = """###\n###\n###\n###\n###\n"""
            rec.display()
            got = output.getvalue()
            self.assertEqual(got, expected)

        rec = Rectangle(3, 5, 1, 1)
        with patch('sys.stdout', new=StringIO()) as output:
            expected = """\n ###\n ###\n ###\n ###\n ###\n"""
            rec.display()
            got = output.getvalue()
            self.assertEqual(got, expected)

    def test_rectangle_update_args(self):
        """Test the update method of the Rectangle, with *args"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (89) 4/5 - 2/3")
        # Check for large number of arguments
        r.update(16, 5, 7, 10, 3, 21, 44, 71, 0)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (16) 10/3 - 5/7")

    def test_rectangle_update_kwargs(self):
        """Test the update method of the Rectangle, with **kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=1)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (10) 10/10 - 10/1")
        r.update(width=5, y=3, x=2)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (10) 2/3 - 5/1")
        r.update(x=7, id=18)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (18) 7/3 - 5/1")

    def test_rectangle_update_args_and_kwargs(self):
        """Test the update method of the Rectangle, with *args and **kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(20, height=1, width=7, x=3, y=9)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (20) 10/10 - 10/10")
        r.update(20, 5, 3, y=1, x=1)
        self.assertMultiLineEqual(r.__str__(),
                                  "[Rectangle] (20) 10/10 - 5/3")

    def test_rectangle_dictionary(self):
        """Test the dictionary representation of the Rectangle object"""
        r = Rectangle(3, 5, id=4)
        self.assertEqual(r.to_dictionary(),
                         {'width': 3, 'height': 5, 'x': 0, 'y': 0, 'id': 4})
        r.update(x=7, y=3)
        self.assertEqual(r.to_dictionary(),
                         {'width': 3, 'height': 5, 'x': 7, 'y': 3, 'id': 4})

    def test_rectangle_json_string(self):
        """Test the json string representation of the Rectangle"""
        # In this test:
        # Convert a list of Rectangle dictionary to a JSON string
        # Then convert that JSON string back to a list of Rectangle dictionary
        # Compare the original Rectangle dictionary with the converted one
        # This way you can check what got out, is the same as what got in.

        rec = Rectangle(3, 5, id=4)
        rec_json_string = rec.to_json_string([rec.to_dictionary()])
        rec_dict = rec.from_json_string(rec_json_string)
        self.assertEqual([rec.to_dictionary()], rec_dict)

        rec.update(x=7, y=3)
        rec_json_string = rec.to_json_string([rec.to_dictionary()])
        rec_dict = rec.from_json_string(rec_json_string)
        self.assertEqual([rec.to_dictionary()], rec_dict)

    def test_rectangle_save_json_file(self):
        """Test saving the Rectangle to a JSON file"""
        rec1 = Rectangle(3, 5, id=4)
        rec2 = Rectangle(16, 28, 1, 3, 70)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            got = Rectangle.from_json_string(file.read().rstrip('\n'))
            exp = [rec1.to_dictionary(), rec2.to_dictionary()]
            self.assertEqual(got, exp)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            got = Rectangle.from_json_string(file.read().rstrip('\n'))
            exp = []
            self.assertEqual(got, exp)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            got = Rectangle.from_json_string(file.read().rstrip('\n'))
            exp = []
            self.assertEqual(got, exp)

    def test_rectangle_create(self):
        """Test the create method of Rectangle"""
        rec1 = Rectangle(3, 5, id=4)
        rec1_dict = rec1.to_dictionary()
        rec2 = rec1.create(**rec1_dict)
        rec2_dict = rec2.to_dictionary()
        self.assertIsInstance(rec2, Rectangle)
        self.assertEqual(rec1_dict, rec2_dict)

    def test_rectangle_load_from_file(self):
        """Test loadings Rectangle instances from a file"""
        rec1 = Rectangle(3, 5, id=4)
        rec2 = Rectangle(16, 28, 1, 3, 70)
        Rectangle.save_to_file([rec1, rec2])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(len(list_objs), 2)
        self.assertEqual(list_objs[0].to_dictionary(), rec1.to_dictionary())
        self.assertEqual(list_objs[1].to_dictionary(), rec2.to_dictionary())

    def test_rectangle_save_csv_file(self):
        """Test saving the Rectangle to a CSV file"""
        rec1 = Rectangle(3, 5, id=4)
        rec2 = Rectangle(16, 28, 1, 3, 70)
        Rectangle.save_to_file_csv([rec1, rec2])
        list_objs = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_objs), 2)
        self.assertEqual(list_objs[0].to_dictionary(), rec1.to_dictionary())
        self.assertEqual(list_objs[1].to_dictionary(), rec2.to_dictionary())

        Rectangle.save_to_file_csv([])
        got = Rectangle.load_from_file_csv()
        exp = []
        self.assertEqual(got, exp)

        Rectangle.save_to_file_csv(None)
        got = Rectangle.load_from_file_csv()
        exp = []
        self.assertEqual(got, exp)
