# 0x01. Python - if/else, loops, functions

## Mandatory

[0-positive_or_negative.py](./0-positive_or_negative.py)

- A python script that generates a random number and prints whether the number
  is positive, negative, or zero.

[1-last_digit.py](./1-last_digit.py)

- A python script that generates a random number and prints whether the last
  digit of that number is greater than 5, is less than 6 and not 0, or is 0.

[2-print_alphabet.py](./2-print_alphabet.py)

- A python script that prints the lowercase alphabets, not followed by a new
  line.
- The script must only use the 'str.format' string formatter and one loop.

[3-print_alphabt.py](./3-print_alphabt.py)

- A python script that prints the lowercase alphabets, except the characters
  'q' and 'a', not followed by a new line.
- The script must only use the 'str.format' string formatter and one loop.

[4-print_hexa.py](./4-print_hexa.py)

- A python script that prints numbers and hexadecimals from 0 to 98.
- The script must only use the 'str.format' string formatter and one loop.

[5-print_comb2.py](./5-print_comb2.py)

- A python script that prints numbers from 0 to 99.
- Numbers are separated by a comma and a space, except the last number which is
  followed by a new line.

[6-print_comb2.py](./6-print_comb3.py)

- A python script that prints all possible different combinations of two digits.
- The numbers are separated by a comma and a space, except for the last number
  which is followed by a new line.

[7-islower.py](./7-islower.py)

- A python function that returns True if a character is lowercase, or False if
  it is not.

[8-uppercase.py](./8-uppercase.py)

- A python function that converts and prints all lowercase letters in a string
  to uppercase.

[9-print_last_digit.py](./9-print_last_digit.py)

- A python script that prints and returns the last digit of a number.

[10-add.py](./10-add.py)

- A python function that returns the sum of two numbers.

[11-pow.py](./11-pow.py)

- A python function that two numbers 'a' and 'b', and returns 'a' to the power
  of 'b'.

[12-fizzbuzz.py](./12-fizzbuzz.py)

- A python function that prints numbers from 1 to 100, but for numbers which are
  multiples of 3 print 'Fizz', and numbers which are multiples of 5 print
  'Buzz', and for numbers which are multiples of both 3 and 5 print 'FizzBuzz'.

[13-insert_number.c](./13-insert_number.c), [lists.h](./lists.h)

- A function in C that inserts a number into a sorted singly linked list.
- To test the function:
  - compile using the following command:
    `gcc -Wall -Wextra -Werror -pedantic -std=gnu89 13-insert_number.c mains/13-linked_lists mains/13-main.c`
  - then simply run the executable: `./a.out`

## Advanced

[100-print_tebahpla.py](./100-print_tebahpla.py)

- A python script that prints the ASCII alphabet, in reverse order, alternating
  lowercase and uppercase (z in lowercase and Y in uppercase), not followed by
  a new line.

[101-remove_char_at.py](./101-remove_char_at.py)

- A function that creates a copy of the string, removing the character at the
  position n (not the Python way, the “C array index”).

[102-magic_calculation.py](./102-magic_calculation.py)

- A python function that does exactly the same as the following Python bytecode

```python
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
