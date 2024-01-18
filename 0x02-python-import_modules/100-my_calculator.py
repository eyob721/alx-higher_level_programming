#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    from calculator_1 import add, div, mul, sub

    # Check for the correct number of arguments
    script_argc = len(argv) - 1
    if script_argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Next check for supported operators
    opr = argv[2]
    opr_table = {"+": add, "-": sub, "*": mul, "/": div}
    if opr not in opr_table:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # Get the operator function, for the given operator
    opr_func = opr_table[opr]

    # Perform the operation
    a = int(argv[1])
    b = int(argv[3])
    result = opr_func(a, b)
    print("{} {} {} = {}".format(a, opr, b, result))
