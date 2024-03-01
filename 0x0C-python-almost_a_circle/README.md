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

## Files

- In this project we work on three classes, the `Base` class, the `Rectangle`
  class and the `Square` class.
- The files containing these classes can be found in the `models/` directory.
  - [models/base.py](./models/base.py)
  - [models/rectangle.py](./models/rectangle.py)
  - [models/square.py](./models/square.py)
- The test files for each class can be found in the directory `tests/test_models`
  - [tests/test_models/test_base.py](./tests/test_models/test_base.py)
  - [tests/test_models/test_rectangle.py](./tests/test_models/test_rectangle.py)
  - [tests/test_models/test_square.py](./tests/test_models/test_square.py)
- There are also additional main scripts in the `mains/` directory that can be
  used as a test for each individual task.

## Mandatory

### Task 0 - Tests

- Prepare a `tests` directory for test files.
- Add `__init__.py` to make it a Python package and importable.

### Task 1 - Base

- Create a directory named `models` with an empty `__init__.py` file, to make
  the directory a Python package.
- Create a file `models/base.py` and write the first class `Base`.
- This class contains a public instance attribute `id` and a private class
  attribute `__nb_objects`.
- This class will be the base of all other classes in this project.
- The goal is to manage the `id` attribute in all future classes and avoid code
  duplication.

### Task 2 - Rectangle

- `models/rectangle.py` is a module that contains a class `Rectangle` which
  inherits from `Base`.
- Rectangle contains the private instance attributes `width`, `height`, `x` and
  `y`.

### Task 3 - Rectangle

- Add validation for all setters of the private instance attributes `width`,
  `height`, `x` and `y`.

### Task 4 - Rectangle

- Add a public instance method `area(self)` that returns the area of the rectangle.

### Task 5 - Rectangle

- Add a public instance method `display(self)` that prints the rectangle to stdout
  using the `#` character.

### Task 6 - Rectangle

- Add a public instance method `__str__(self)` to override the string representation
  of the rectangle object.

### Task 7 - Rectangle

- Update the `display(self)` method to adjust for `x` and `y` position when
  printing.

### Task 8 - Rectangle

- Add a public instance method `update(self, *args)` that updates the value of the
  attributes of the Rectangle object.

### Task 9 - Rectangle

- Update the `update(self, *args)` method to hold keyword variable arguments as
  well, in addition to the positional variable arguments.
- So the method will be modified to `update(self ,*args, **kwargs)`.
- If `*args` is given then `**kwargs` is ignored

### Task 10 - Square

- Write a class `Square` that inherits from `Rectangle`.
- Override the `__str__(self)` method of the Rectangle class in the Square class.

### Task 11 - Square

- Add a public getter and setter for the `size` attribute of the `Square`.

### Task 12 - Square

- Overload the `update(self, *args, **kwargs)` method of the Rectangle class
  in the Square class.

### Task 13 - Square

- Add a public instance method `to_dictionary(self)` that returns the dictionary
  representation of the `Rectangle` object.

### Task 14 - Square

- Add a public instance method `to_dictionary(self)` that returns the dictionary
  representation of the `Square` object.

### Task 15 - Base

- Add a static method `to_json_string(list_dictionaries)` that returns the JSON
  string representation of a list of dictionaries.

### Task 16 - Base

- Add a public class method `save_to_file(cls, list_objs)` that writes the JSON
  string representation of a list of objects to a file.
- All objects in the list `list_objs` inherit from `Base`

### Task 17 - Base

- Add a static method `from_json_string(json_string)` that returns A Python
  list of dictionaries from a JSON String

### Task 18 - Base

- Add a class method `create(cls, **dictionary)` that returns an instance of the
  Rectangle or Square class, based on whichever class is calling the method,
  with all the attributes set from a given dictionary.

### Task 19 - Base

- Add a class method `load_from_file(cls)` that returns list of instances.
- The instances are of Rectangle or Square class.
- The method must use `from_json_string` and `create` methods.

## Advanced

### Task 20 - Base

- Add the class methods `save_from_file_csv(cls)` and `load_from_file_csv(cls)`
  that serializes and deserializes in CSV.
- The methods have the same behaviors as the JSON serialization/deserialization

### Task 21 - Base

- Add a static method `draw(list_rectangles, list_squares)` that opens a window
  using the turtle graphics module and draws all the Rectangles and Squares in
  the lists.
