#!/usr/bin/python3
for i in range(122, 96, -1):
    k = i
    if (k % 2 != 0):
        k -= 32
    print("{}".format(chr(k)), end='')
