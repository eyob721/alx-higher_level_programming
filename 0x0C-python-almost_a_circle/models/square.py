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

    def __str__(self):
        """Informal string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
