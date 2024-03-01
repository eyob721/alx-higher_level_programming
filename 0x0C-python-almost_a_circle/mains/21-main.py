#!/usr/bin/python3
"""Task 19"""
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from models.base import Base  # noqa
from models.rectangle import Rectangle  # noqa
from models.square import Square  # noqa

if __name__ == "__main__":

    list_rectangles = [
        Rectangle(100, 40),
        Rectangle(90, 110, 30, 10),
        Rectangle(20, 25, 110, 80),
    ]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
