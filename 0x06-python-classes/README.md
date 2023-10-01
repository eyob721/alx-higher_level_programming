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
