#!/usr/bin/python3
if (__name__ == "__main__"):
    from sys import argv
    actual_argc = len(argv)
    script_argc = actual_argc - 1
    argc_message = ""

    if (script_argc == 0):
        argc_message += "arguments."
    elif (script_argc == 1):
        argc_message += "argument:"
    else:
        argc_message += "arguments:"

    print("{} {}".format(script_argc, argc_message))
    i = 1
    while (i < actual_argc):
        print("{}: {}".format(i, argv[i]))
        i += 1
