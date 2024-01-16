#!/usr/bin/python3
for i in range(122, 96, -1):
    k = i - 32 if i % 2 != 0 else i
    print("{}".format(chr(k)), end="")
