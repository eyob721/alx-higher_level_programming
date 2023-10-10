"""A module for task 10."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class definition of a Square."""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of Square"""
        return self.__size ** 2
