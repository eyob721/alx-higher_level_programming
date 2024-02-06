# 0x06. Python - Classes and Objects

## Mandatory

[0-square.py](./0-square.py)

- A module that contains an empty class of a Square object.

[1-square.py](./1-square.py)

- Building on the previous module (0-square.py), we add a private instance
  attribute, called `size`, to the Square class.

[2-square.py](./2-square.py)

- Building on the previous module (1-square.py), we validate the size
  attribute, so that only an object of type int and a value of >= 0 is
  accepted as a valid size.
- Otherwise it will raise TypeError and ValueError respectively.

[3-square.py](./3-square.py)

- Building on the previous module (2-square.py), we add the public instance
  method, called `area` that returns the current square objects area.

[4-square.py](./4-square.py)

- Building on the previous module (3-square.py), we add getter and setter
  methods by way of property decorator.

[5-square.py](./5-square.py)

- Building on the previous module (4-square.py), we add a public instance
  method that prints the square with the `#` character.

[6-square.py](./6-square.py)

- Building on the previous module (5-square.py), we add a `position` attribute
  that contains the current position in the square.
- The method that is used to print the square is adjusted to include the new
  `position` attribute as well.

## Advanced

[100-main.py](./100-main.py)

- A module that contains a `Node` class and a `SinglyLinkedList` class to
  implement singly linked lists.

[101-square.py](./101-square.py)

- Building on the previous module (6-square.py), we add the `__str__()` method
  to print the square when referenced, just as it would when we call the method
  that is used to print the square.

[102-square.py](./102-square.py)

- Building on the previous module (4-square.py), we add comparison capability
  of two `Square` objects by overriding the comparison methods.

[103-magic_class.py](./103-magic_class.py)

- A Python class named `MagicClass` that does exactly as the following Python Bytecode.

```python
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```
