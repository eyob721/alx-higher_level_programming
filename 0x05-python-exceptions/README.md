# 0x05. Python - Exceptions

## Mandatory

[0-safe_print_list.py](./0-safe_print_list.py)

- A function that prints `x` elements from a list.
- The list can contain items of any type.
- `x` can be bigger than the length of the list.
- `try: / except:` clauses must be used.

[1-safe_print_integer.py](./1-safe_print_integer.py)

- A function that takes an object and prints it, if it is an integer.
- The function must use `{:d}.format()` to print the integer.
- `try: / except:` clauses must be used.

[2-safe_print_list_integers.py](./2-safe_print_list_integers.py)

- A function that prints the first `x` elements from a list if they are
  integers.
- The list can contain items of any type.
- The function must use `{:d}.format()` to print the integer.
- `try: / except:` clauses must be used.

[3-safe_print_division.py](./3-safe_print_division.py)

- A function that divides 2 integers and prints the result.
- It is assumed that the arguments are integers.
- The result of the division must be printed in the `finally:` clause.
- `try: / except: / finally:` clauses must be used.

[4-list_division.py](./4-list_division.py)

- A function that divides two lists element by element.
- The lists can contain items of any type.
- And the lists can also be of any length.
- It returns a list containing the result of the division.
- If an exception is raised a value of 0 is used in the returned result list.
- `try: / except: / finally:` clauses must be used.

[5-raise_exception.py](./5-raise_exception.py)

- A function that raises a type exception.

[6-raise_exception_msg.py](./6-raise_exception_msg.py)

- A function that raises a name exception with a message.

## Advanced

[100-safe_print_integer_err.py](./100-safe_print_integer_err.py)

- A function that prints an integer.
- The function can take as an arguments an object of any type.
- The function must use `{:d}.format()` to print the integer.
- `try: / except:` clauses must be used.
- If an exception is raised it must print the appropriate message to stderr.

[101-safe_function.py](./101-safe_function.py)

- A function that executes a function safely.
- If an exception is raised it must print the appropriate message to stderr.

[102-magic_calculation.py](./102-magic_calculation.py)

- A python function `def magic_calculation(a, b)` that does exactly the same
  as the following bytecode:

```python
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
    106 RETURN_VALUE
```

[103-python.c](./103-python.c)

- Contains three C functions that print some basic info about a Python list
  object, a Python bytes object and a Python float object.
- NOTE: The file must be compiled with the following command:

```sh
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
```

- You can replace the `/usr/include/python3.4` part of the command with what
  ever version of python you are using, for example if you have python3.8 use
  `/usr/include/python3.8`.
