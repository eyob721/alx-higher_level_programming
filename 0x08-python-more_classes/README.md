# 0x08. Python - More Classes and Objects

## Mandatory

[0-rectangle.py](./0-rectangle.py)

- A module that contains an empty class definition of a Rectangle object.

[1-rectangle](./1-rectangle.py)

- Building on the previous module (0-rectangle), we add two private instance
  attributes, `width` and `height`.

[2-rectangle](./2-rectangle.py)

- Building on the previous module (1-rectangle), we add the `area` and
  `perimeter` public instance methods that return the area and perimeter of the
  Rectangle object respectively.

[3-rectangle](./3-rectangle.py)

- Building on the previous module (2-rectangle), we define the informal string
  representation of the Rectangle object.
- Informal string representation is accessed when calling `print()` or `str()`.

[4-rectangle](./4-rectangle.py)

- Building on the previous module (3-rectangle), we define the official string
  representation of the Rectangle object.
- Official string representation is accessed when calling `repr()`.
- Using this representation we can recreate a new instance of the current object
  using `eval()`.

[5-rectangle.py](./5-rectangle.py)

- Building on the previous module (4-rectangle), we define a deleter method for
  the Rectangle object.

[6-rectangle.py](./6-rectangle.py)

- Building on the previous module (5-rectangle), we add a public class attribute
  that keeps track of the current number of instances of the Rectangle class.

[7-rectangle.py](./7-rectangle.py)

- Building on the previous module (6-rectangle), we add a public class attribute
  that holds the value of an object used to print the informal representation of
  the Rectangle.

[8-rectangle.py](./8-rectangle.py)

- Building on the previous module (7-rectangle), we add a static method that
  compares two rectangle objects and returns the one with the biggest area.

[9-rectangle.py](./9-rectangle.py)

- Building on the previous module (8-rectangle), we add a class method that
  returns a new Rectangle object with the width and height set to a given size.
  (i.e. a square)

## Advanced

[101-nqueens.py](./101-nqueens.py)

- A solution to the N queens problem.
