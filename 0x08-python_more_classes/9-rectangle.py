#!/usr/bin/python3
"""Task 9"""


class Rectangle:
    """Class definition of a Rectangle

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
        area (int): area of the rectangle
        perimeter (int): perimeter of the rectangle
        number_of_instances (int): number of instances created
        print_symbol (obj): used as symbol for informal string representation

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle constructor

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self) -> int:
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value) -> None:
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """Area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Perimeter of the Rectangle"""
        return (
            0
            if self.__width == 0 or self.__height == 0
            else 2 * (self.__width + self.__height)
        )

    def __str__(self) -> str:
        """Informal string representation of the Rectangle"""
        return (
            ""
            if self.__width == 0 or self.__height == 0
            else (
                (str(self.print_symbol) * self.__width + "\n") * self.__height
            ).rstrip("\n")
        )

    def __repr__(self) -> str:
        """Formal string representation of the Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self) -> None:
        """Gets called when the Rectangle object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a Rectangle with `width` == `height` == `size`"""
        return cls(size, size)
