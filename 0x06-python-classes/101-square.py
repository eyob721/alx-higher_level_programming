#!/usr/bin/python3
"""A module for Task 8."""


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
                if type(i) is not int or i < 0:
                    position_is_not_valid = True
                    break
        if position_is_not_valid:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of the square object.

        Returns:
            int: Area of the square object.

        """
        return self.__size * self.__size

    def my_print(self):
        print("".join(self.__str__()))

    def __str__(self):
        """Write the square using the `#` character.

        Description:
            This function builds a string representation of the square to be
            printed on stdout. If the size of the square is 0, then only a new
            line is printed.Other wise the square is printed using the `#`
            character, adjusting for vertical and horizontal position.

        """
        if self.__size == 0:
            return '\n'

        # Add the vertical position to the square list
        sqr_list = ['\n' for y in range(self.__position[1])]
        for i in range(self.__size):
            # Add the horizontal position to the square list
            sqr_list += [' ' for x in range(self.__position[0])]
            # Write the `#` characters, and the new line at the end
            sqr_list += ['#' for c in range(self.__size)] + ['\n']

        return "".join(sqr_list)
