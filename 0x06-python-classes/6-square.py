#!/usr/bin/python3
"""A module for Task 6."""


class Square:
    """A class that defines a Square object.

    Args:
        size (int): Initial size of the square object. Defaults to 0.
            It must be an integer and >= 0.
        position (tuple): Initial position of the square object.
            Defaults to (0, 0). It must be a tuple of 2 integers.

    Note:
        The position attribute determines the position of the square on stdout.

    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square object.

        Returns:
            int: Area of the square object.

        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using the `#` character, in the current position.
        """
        if self.__size == 0:
            print()
            return

        sqr_i = pos_i = 0
        sqr_size = self.area()
        x, y = self.position

        # Adjust for vertical position
        while pos_i < y:
            print()
            pos_i += 1

        while sqr_i < sqr_size:
            # Adjust for horizontal position
            pos_i = 0
            while sqr_i % self.__size == 0 and pos_i < x:
                print(" ", end="")
                pos_i += 1
            # print # character
            print('#', end="")
            sqr_i += 1
            # print new line
            if (sqr_i % self.__size == 0):
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        position_is_not_valid = False
        if type(value) is not tuple or len(value) != 2:
            position_is_not_valid = True
        else:
            for i in value:
                if type(i) is not int:
                    position_is_not_valid = True
                    break
        if position_is_not_valid:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
