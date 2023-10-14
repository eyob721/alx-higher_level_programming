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

- For the `Rectangle` class, add validation for all setters of the private
  instance attributes `width`, `height`, `x` and `y`.

### Task 4

[models/rectangle.py](./models/rectangle.py)<br>
`test file:` [tests/test_rectangle.py](./tests/test_rectangle.py)

- For the `Rectangle` class, add a public instance method `area` that returns
  the area of the rectangle.
