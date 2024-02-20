# 0x0B. Python - Input/Output

## Mandatory

[0-read_file.py](./0-read_file.py)

- A function that reads a file in `utf-8` encoding and prints it to stdout.

[1-write_file.py](./1-write_file.py)

- A function that writes a text to a file in `utf-8` encoding.
- The function creates the file, if the file doesn't exist.

[2-append_write.py](./2-append_write.py)

- A function that appends a text to a file in `utf-8` encoding.
- The function creates the file, if the file doesn't exist.

[3-to_json_string.py](./3-to_json_string.py)

- A function that returns the JSON string representation of an object.

[4-from_json_string.py](./4-from_json_string.py)

- A function that returns an object from a JSON string representation.

[5-save_to_json_file.py](./5-save_to_json_file.py)

- A function that writes the JSON string representation of an object to a file.

[6-load_from_json_file.py](./6-load_from_json_file.py)

- A function that returns a Python object from a JSON string stored in a file.

[7-add_item.py](./7-add_item.py)

- A script that adds all its arguments to a Python list and saves them to a json
  file.
- The script must use `save_to_json_file` and `load_from_json_file` functions
  from files `5-save_to_json_file.py` and `6-load_from_json_file.py`.

[8-class_to_json.py](./8-class_to_json.py)

- A function that returns the dictionary description of an object.

[9-student.py](./9-student.py)

- A class definition of `Student` that contains `first_name`, `last_name`, and
  `age` public instance attributes as well as a `to_json` publci instance method
  that returns the dictionary description of it self.

[10-student.py](./10-student.py)

- A module based on `9-student` that adds a filter to the `to_json` method.

[11-student.py](./11-student.py)

- A module based on `10-student` that adds a method `reload_from_json` which
  replaces all attributes of the Student instance, given a dictionary of
  attributes.

[12-pascal_triangle.py](./12-pascal_triangle.py)

- A function that returns list of lists of integers representing the Pascal's
  triangle.

## Advanced

[100-append_after.py](./100-append_after.py)

- A functoin that inserts a line of text to a file after each line containing
  a specific string.

[101-stats](./101-stats.py)

- A script that reads `stdin` line by line and computes metrics.
- Every 10 lines or a Keyboard interupt signal (`CTRL + C`) is sent it prints
  the current log status.
