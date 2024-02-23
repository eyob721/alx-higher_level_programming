#!/usr/bin/python3
"""Task 8"""
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from models.rectangle import Rectangle  # noqa

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update()
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

    r1.update(89, 2, 3, 4, 5, 10)
    print(r1)
