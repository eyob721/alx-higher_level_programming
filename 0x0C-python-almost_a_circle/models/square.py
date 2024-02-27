#!/usr/bin/python3
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor

        Args:
            size (int): size of the square
            x (int): x position of the square
            y (int): y position of the square
            id (int): id of the square

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """Informal string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle using args or kwargs"""
        valid_attributes = ["id", "size", "x", "y"]

        if args:
            for attr, value in dict(zip(valid_attributes, args)).items():
                setattr(self, attr, value)
            return

        for key, value in kwargs.items():
            if key in valid_attributes:
                setattr(self, key, value)
