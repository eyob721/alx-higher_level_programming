#!/usr/bin/python3
"""A module for task 6."""


class Rectangle:
    """Class definition of a Rectangle object.

    Attributes:
        number_of_instances (int): Number of Rectangle instances created.

    """
    number_of_instances = 0

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
            The Rectangle object is written using the `#` character, and if
            either of the width or height is 0, then it is an empty string.

        """
        if self.width == 0 or self.height == 0:
            return ""
        rec_list = (['#'] * self.width + ['\n']) * self.height
        rec_list.pop()  # Remove the last new line
        return "".join(rec_list)

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
