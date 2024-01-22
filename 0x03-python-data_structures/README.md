# 0x03. Python - Data Structures: Lists, Tuples

## Mandatory

[0-print_list_integer.py](./0-print_list_integer.py)

- A function that prints all integers of a list.
- NOTE: It is assumed that the list contains only integers.

[1-element_at.py](./1-element_at.py)

- A function that retrieves an element from a list like in C.

[2-replace_in_list.py](./2-replace_in_list.py)

- A function that replaces an element of a list at a specific
  position (like in C).

[3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)

- A function that prints all integers of a list, in reverse order.
- NOTE: It is assumed that the list contains only integers.

[4-new_in_list.py](./4-new_in_list.py)

- A function that replaces an element of a list without modifying the original
  list.

[5-no_c.py](./5-no_c.py)

- A function that removes all characters 'c' and 'C' from a string.

[6-print_matrix_integer.py](./6-print_matrix_integer.py)

- A function that prints a matrix of integers.
- The integers must not be converted into strings.
- It is assumed that the matrix contains integers only.

[7-add_tuple.py](./7-add_tuple.py)

- A function that adds two tuples of integers and returns their sum in tuple
  form.

[8-multiple_returns.py](./8-multiple_returns.py)

- A function that returns a tuple with the length of a string and
  its first character.

[9-max_integer.py](./9-max_integer.py)

- A function that finds the maximum integer in a list.
- The list is assumed to contain only integers and using built in
  `max()` in not allowed.

[10-divisible_by_2.py](./10-divisible_by_2.py)

- A function that finds all multiples of 2 in a list.
- The function returns a new list with `True` or `False`, depending on
  whether the integer at the same position in the original list is a
  multiple of 2.

[11-divisible_by_2.py](./11-delete_at.py)

- A function that deletes the item at a specific position in a list.

[12-switch.py](./12-switch.py)

- A simple script that switches the value of two integers.
- Only line 4 must be edited, and the script must be 5 line long.

[lists.h](./lists.h), [13-is_palindrome.c](./13-is_palindrome.c)

- A C function that checks if a singly linked list is a palindrome or not.
- To test the function:
  - compile using the following command:
    `gcc -Wall -Wextra -Werror -pedantic -std=gnu89 13-is_palindrome.c mains/13-linked_lists mains/13-main.c -o palindrome`
  - then simply run the executable: `./palindrome`

## Advanced

[100-print_python_list_info.c](./100-print_python_list_info.c)

- A C function that prints some basic info about Python lists.
- NOTE: The function must be compiled with following command:
  `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
- You can replace the `/usr/include/python3.4` part of the command with what
  ever version of python you are using, for example if you have python3.8 use
  `/usr/include/python3.8`.
