# 0x00. Python - Hello, World

## Mandatory

[0-run](./0-run)

- A shell script that runs a python script.
- The path to the python script must be saved in an environment variable PYFILE

[1-run_inline](./1-run_inline)

- A shell script that runs a python code.
- The python code  must be saved in an environment variable PYCODE

[2-print.py](./2-print.py)

- A python script that prints a string.

[3-print_number.py](./3-print_number.py)

- A python script that uses f-stings to print an integer stored in a variable
  followed by a string "Batter street".

[4-print_float.py](./4-print_float.py)

- A python script that uses f-stings to print a float stored in a variable.

[5-print_string.py](./5-print_string.py)

- A python script that prints the string stored in a variable three times,
  followed by a new line, and the print the first 9 characters of the variable.
- No loops allowed.

[6-concat.py](./6-concat.py)

- A python script that concatenates two string variables and prints them.

[7-edges.py](./7-edges.py)

- A python script that prints slices of sting variable

[8-concat_edges.py](./8-concat_edges.py)

- A python script that prints "object-oriented programming with python" by
  slicing a given string variable, without using loops.

[9-easter_egg.py](./9-easter_egg.py)

- A python script that prints "The Zen of Python", by Tim Peters, followed by a
  new line.
- The script must have a maximum of 98 characters.

[10-check_cycle.c](./10-check_cycle.c), [lists.h](./lists.h)

- A c function that check if a singly linked list has a cycle or not.
- To test the function:
  - compile using the following command:
    `gcc -Wall -Wextra -Werror -pedantic -std=gnu89 10-check_cycle.c mains/10-linked_lists mains/10-main.c -o check_cycle`
  - then simply run the executable: `./check_cycle`

## Advanced

[100-write.py](./100-write.py)

- A python script that prints a string to stderr and exits with code 1, without
  using the print function.

[101-compile](./101-compile)

- A shell script that compiles python source files and outputs the bytecode.

[102-magic_calculation.py](./102-magic_calculation.py)

- A python function that does exactly the same as the following python bytecode.

```bytecode
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
