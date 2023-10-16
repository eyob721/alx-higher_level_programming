# 0x0C. Python - Almost a circle

In this project we review everything we have learned on Python. Things like:

- import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- File read/write
- args and kwargs
- Serialization/Deserialization
- JSON

## Mandatory

### Task 0

[tests/](./tests)

- Prepare a `tests` directory for test files.
- Add `__init__.py` to make it a Python package and importable.

### Task 1

[models/__init__.py](./models/__init__.py)<br>
[models/base.py](./models/base.py)<br>
`test file:` [tests/test_base.py](./tests/test_base.py)

- Create a directory named `models` with an empty `__init__.py` file, to make
  the directory a Python package.
- Create a file `models/base.py` and write the first class `Base`.
- This class contains a public instance attribute `id` and a private class
  attribute `__nb_objects`.
- This class will be the base of all other classes in this project.
- The goal is to manage the `id` attribute in all future classes and avoid code
  duplication.

### Task 2

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- `models/rectangle.py` is a module that contains a class `Rectangle` which
  inherits from `Base`.
- Rectangle contains the private instance attributes `width`, `height`, `x` and
  `y`.

### Task 3

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- Add validation for all setters of the private instance attributes `width`, 
  `height`, `x` and `y`.

### Task 4

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- Add a public instance method `area()` that returns the area of the rectangle.

### Task 5

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- Add a public instance method `display()` that prints the rectangle to stdout
  using the `#` character.

### Task 6

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- Add a public instance method `__str__()` to override the string representation
  of the rectangle object.

### Task 7

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- Update the `display()` method to adjust for `x` and `y` position when printing.

### Task 8

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- Add a public instance method `update()` that updates the value of the
  attributes of the Rectangle object.

### Task 9

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- Update the `update()` method to hold keyword variable arguments as well, in
  addition to the positional variable arguments.

### Task 10

[models/square.py](./models/square.py)<br>
`test file:` [tests/test_square.py](./tests/test_square.py)

- Write a class `Square` that inherits from `Rectangle`.
- Override the `__str__()` method of the Rectangle class in the Square class.

### Task 11

[models/square.py](./models/square.py)<br>
`test file:` [tests/test_square.py](./tests/test_square.py)

- Add a public getter and setter for the `size` attribute of the `Square`.

### Task 12

[models/square.py](./models/square.py)<br>
`test file:` [tests/test_square.py](./tests/test_square.py)

- Overload the `update()` method of the Rectangle class in the Square class.

### Task 13

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- Add a public instance method `to_dictionary()` that returns the dictionary
  representation of the `Rectangle` object.

### Task 14

[models/square.py](./models/square.py)<br>
`test file:` [tests/test_square.py](./tests/test_square.py)

- Add a public instance method `to_dictionary()` that returns the dictionary
  representation of the `Square` object.

### Task 15

[models/base.py](./models/base.py)<br>
`test file:` [tests/test_base.py](./tests/test_base.py)

- Add a static method `to_json_string()` that returns the JSON string
  representation of Base.

### Task 16

[models/base.py](./models/base.py)<br>
`test file:` [tests/test_base.py](./tests/test_base.py)

- Add a public class method `save_to_file()` that writes the JSON string
  representation of objects that inherit from `Base` to a file.

### Task 17

[models/base.py](./models/base.py)<br>
`test file:` [tests/test_base.py](./tests/test_base.py)

- Add a static method `from_json_string()` that returns A Python list of
  dictionaries from a JSON String

### Task 18

[models/base.py](./models/base.py)<br>
`test file:` [tests/test_base.py](./tests/test_base.py)

- Add a class method `create(cls, **dictionary)` that returns an instance of the
  Rectangle or Square class, based on whichever class is calling the method,
  with all the attributes set from a given dictionary.
