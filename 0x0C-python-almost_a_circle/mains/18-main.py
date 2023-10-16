#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square


if __name__ == "__main__":

    r1 = Rectangle(3, 5, id=12)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

    sqr1 = Square(3, id=21)
    sqr1_dictionary = sqr1.to_dictionary()
    sqr2 = Square.create(**sqr1_dictionary)
    print(sqr1)
    print(sqr2)
    print(sqr1 is sqr2)
    print(sqr1 == sqr2)
