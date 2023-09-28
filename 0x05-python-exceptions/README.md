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
