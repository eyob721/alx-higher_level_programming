#!/usr/bin/python3
"""Task 9"""


def magic_calculation(a, b):
    """Function derived from given bytecode"""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a**b) / i
        except Exception:
            result = b + a
            break
    return result
