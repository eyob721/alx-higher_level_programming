#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for c in str:
        c_ascii = ord(c)
        str_upper += chr(c_ascii - 32) if 97 <= c_ascii <= 122 else c
    print("{}".format(str_upper))
