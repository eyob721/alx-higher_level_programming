#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    script_argc = len(argv) - 1

    if script_argc == 0:
        argc_message = "arguments."
    elif script_argc == 1:
        argc_message = "argument:"
    else:
        argc_message = "arguments:"

    print("{} {}".format(script_argc, argc_message))
    i = 1
    while i <= script_argc:
        print("{}: {}".format(i, argv[i]))
        i += 1
