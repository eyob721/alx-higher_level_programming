#!/usr/bin/python3
def print_last_digit(number):
    number *= -1 if number < 0 else 1
    digit = number % 10
    print("{:d}".format(digit), end="")
    return digit
