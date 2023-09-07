#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4
    names = dir(hidden_4)
    names_count = len(names)
    i = 0
    while (i < names_count):
        if (names[i][0] != '_'):
            print(names[i])
        i += 1
