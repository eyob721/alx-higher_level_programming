#!/usr/bin/python3
"""A module for task 8."""


class Rectangle:
    """Class definition of a Rectangle object.

    Attributes:
        number_of_instances (int): Number of Rectangle instances created.
        print_symbol (obj): Used as a symbol for informal string
                            representation.

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation.

        Args:
            width (int): width of the new Rectangle object
            height (int): height of the new Rectangle object

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the Rectangle object."""
        return self.__width

    @width.setter
    def width(self, value):
        """Assigns `value` to the width of the Rectangle object.

        Args:
            value (obj): A given value for the width of the Rectangle object.

        Raises:
            TypeError: If the 'value' is not an integer
            ValueError: If the `value` is < 0

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        """Assigns `value` to the height of the Rectangle object.

        Args:
            value (obj): A given value for the height of the Rectangle object.

        Raises:
            TypeError: If the 'value' is not an integer
            ValueError: If the `value` is < 0

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle object."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle object."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the informal string representation of the Rectangle.

        Note:
            The Rectangle object is written using whatever object is assigned
            to the `print_symbol` attribute. But In the case that an instance
            attribute of `print_symbol` is cretater, then the value of the
            instance attribute is used. If either of the width or height is 0,
            then it is an empty string.

        """
        if self.width == 0 or self.height == 0:
            return ""
        obj = Rectangle.print_symbol
        if 'print_symbol' in self.__dict__:
            obj = self.print_symbol
        rec_list = ([obj] * self.width + ['\n']) * self.height
        rec_list.pop()  # Remove the last new line
        return "".join([str(i) for i in rec_list])

    def __repr__(self):
        """Return the offical string representation of the Rectangle.

        Note:
            Using this representation it is possible to recreate a new instance
            of the current object using `eval()`.

        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Say Good Bye."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): First Rectangle object
            rect_2 (Rectangle): Second Rectangle object

        Returns:
            The Rectangle object with the bigger or equal area.

        Raises:
            TypeError: If either of `rect_1` or `rect_2` is not a Rectangle.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
