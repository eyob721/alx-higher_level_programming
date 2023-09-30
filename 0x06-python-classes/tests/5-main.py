#!/usr/bin/python3
Square = __import__('5-square').Square

print("\nTest 1 ---------------------")
my_square = Square(3)
my_square.my_print()

print("--")

print("\nTest 2 ---------------------")
my_square.size = 10
my_square.my_print()

print("--")

print("\nTest 3 ---------------------")
my_square.size = 0
my_square.my_print()

print("--")
