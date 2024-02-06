#!/usr/bin/python3
"""Task 6"""


class Square:
    """A class that defines a Square object"""

    def __init__(self, size=0, position=(0, 0)):
        """Square constructor

        Args:
            size: Initial size of the square object
                  It must be an integer and >= 0
            position: Initial position of the square object
                      It must be a tuple of 2 integers

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size of the square object"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position of the square object"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers"
                )
        self.__position = value

    def area(self):
        """Area of the square object

        Returns:
            int: Area of the square object

        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using the # character, in the current position"""
        x = self.position[0]
        y = self.position[1]
        sqr = (
            "\n"
            if self.__size == 0
            else "\n" * y + (" " * x + "#" * self.__size + "\n") * self.__size
        )
        print(sqr, end="")
