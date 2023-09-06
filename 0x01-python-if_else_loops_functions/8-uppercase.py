#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper = c
        if (97 <= ord(c) <= 122):
            upper = chr(ord(c) - 32)
        print("{}".format(upper), end="")
    print()
