#!/usr/bin/python3
import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

divisible_by_2 = __import__("10-divisible_by_2").divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print(
        "{:d} {:s} divisible by 2".format(
            my_list[i], "is" if list_result[i] else "is not"
        )
    )
    i += 1
