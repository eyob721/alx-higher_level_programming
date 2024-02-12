# 0x07. Python - Test-driven development

In this project all the test files for each task are provided in the `tests`
directory. There are doc tests and unit tests in this project.

The doc tests can be checked using the command:

```sh
python3 -m doctest ./tests/<testfile>
```

The unit tests can also be checked using the command:

```sh
python3 -m unittest ./tests/<testfile>
```

## Mandatory

[0-add_integer.py](./0-add_integer.py)<br>
`test:` [0-add_integer.txt](./0-add_integer.txt)

- A module containing a function that adds 2 integers.

[2-matrix_divided.py](./2-matrix_divided.py)<br>
`test:` [2-matrix_divided.txtt](./2-matrix_divided.txt)

- A module containing a function that divides a matrix by a number.

[3-say_my_name.py](./3-say_my_name.py)<br>
`test:` [3-say_my_name.txt](./3-say_my_name.txt)

- A module containing a function that prints first and last name.

[4-print_square.py](./4-print_square.py)<br>
`test:` [4-print_square.txt](./4-print_square.txt)

- A module containing a function that prints a square using `#`.

[5-text_indentation](./5-text_indentation.py)<br>
`test:` [5-text_indentation.txt](./5-text_indentation.txt)

- A module containing a function that prints a text with 2 new lines after
  each of the characters `.`, `?` and `:`

[6-max_integer.py](./6-max_integer.py)<br>
`test:` [6-max_integer_test.py](./6-max_integer_test.py)

- A module containing a function that finds the maximum integer in a list.
- This function is a given function, we are supposed to write a unit test that
  is passable by the given function.

## Advanced

[100-matrix_mul.py](./100-matrix_mul.py)<br>
`test:` [100-matrix_mul.txt](./100-matrix_mul.txt)

- A module containing a function that multiplies tw0 matrices.

[101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py)<br>
`test:` [101-lazy_matrix_mul.txt](./101-lazy_matrix_mul.txt)

- A module containing a function that multiplies two matrices, using the
  `NumPy` module.

[102-python.c](./102-python.c)

- Contains a C function that prints some basic info about a Python string object.
- NOTE: The file must be compiled with the following command:
  ```sh
  gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
  ```
- You can replace the `/usr/include/python3.4` part of the command with what
  ever version of python you are using, for example if you have python3.8 use
  `/usr/include/python3.8`.
