# 0x0A. Python - Inheritance

## Mandatory

[0-lookup.py](./0-lookup.py)

- A function that returns list of attributes and methods of an object.

[1-my_list.py](./1-my_list.py)<br>
`test:` [tests/1-my_list.txt](./tests/1-my_list.txt)

- A module containing a class that inherits from the built in class `list` and
  has its own public instance method that prints the list in sorted ascending
  order.

[2-is_same_class.py](./2-is_same_class.py)

- A module containing a function that returns True if an object is exactly
  an instance of a class.

[3-is_kind_of_class.py](./3-is_kind_of_class.py)

- A module containing a function that returns True if an object is a
  subclass of a class.

[4-inherits_from.py](./4-inherits_from.py)

- A module containing a function that returns True if an object is an instance
  of a class that directly or indirectly inherited from a specified class.

[5-base_geometry.py](./5-base_geometry.py)

- A module containing an empty class of `BaseGeometry`.

[6-base_geometry.py](./6-base_geometry.py)

- A module based on `5-base_geometry`.
- It adds a public instance method `area`.

[7-base_geometry.py](./7-base_geometry.py)<br>
`test:` [tests/7-base_geometry.txt](./tests/7-base_geometry.txt)

- A module based on `6-base_geometry`.
- It adds a public instance method `integer_validator` that validates the value
  of an integer.

[8-rectangle.py](./8-rectangle.py)

- A module containing a class `Rectangle` that inherits from `BaseGeometry`
  class defined in the `7-base_geometry` module.

[9-rectangle.py](./9-rectangle.py)

- A module based on `8-rectangle`.
- It adds an `area` implementation and defines the string representation
  (`__str__`) of the `Rectangle` class.

[10-square.py](./10-square.py)

- A module containing a class `Square` that inherits from `Rectangle` class
  defined in the `9-rectangle` module.

[11-square.py](./11-square.py)

- A module based on `10-square`.
- It adds a string representation (`__str__`) of the `Square` class.

## Advanced

[100-my_int.py](./100-my_int.py)

- A module containing a class `MyInt` that inherits for `int` built in class and
  invertes the operaions of `==` and `!=`.

[101-add_attribute.py](./101-add_attribute.py)

- A module containing a function that adds an attribute to an object, it it's
  possible.
