#!/usr/bin/python3
"""Task 7"""


class BaseGeometry:
    """Class definition of BaseGeometry."""

    def area(self):
        """Area of a shape."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value of an integer.

        Args:
            name (str): Name of the integer. It is assumed to be a string.
            value (int): Value of the integer.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is <= 0

        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
