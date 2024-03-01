#!/usr/bin/python3
"""Base"""
import json


class Base:
    """Base class

    Attributes:
        id (int): id of the object

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor

        Args:
            id (int): id of the object

        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string represenation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        """
        return (
            json.dumps(list_dictionaries)
            if list_dictionaries
            else json.dumps([])
        )

    @staticmethod
    def from_json_string(json_string):
        """Returns a Python list from a JSON string

        Args:
            json_string (str): json string representing a list of dictionaries

        """
        return json.loads(json_string) if json_string else json.loads("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs: list of instances which inherit from Base
                        example: list of Rectangle or list of Square instances

        """
        list_dicts = (
            []
            if not list_objs or type(list_objs) is not list
            else [obj.to_dictionary() for obj in list_objs]
        )
        json_string = cls.to_json_string(list_dicts)

        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(json_string + "\n")

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read().rstrip("\n"))
        except Exception:
            list_objs = []
        else:
            list_objs = [cls.create(**d) for d in list_dicts]
        return list_objs

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            dictionary (dict): a dictionary where key is the attribute name and
                                value is the value of the attribute

        """
        if cls.__name__ == "Rectangle":
            obj = cls(3, 5)  # type: ignore
        else:
            obj = cls(3)
        obj.update(**dictionary)  # type: ignore
        return obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the JSON string representation of list_objs to a CSV file

        Args:
            list_objs: list of instances which inherit from Base
                        example: list of Rectangle or list of Square instances

        """
        file_name = cls.__name__ + ".csv"
        if type(list_objs) is list:
            list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dictionaries = []
        with open(file_name, "w", encoding="utf-8") as file:
            for d in list_dictionaries:
                id = d["id"]
                x = d["x"]
                y = d["y"]
                if cls.__name__ == "Rectangle":
                    width = d["width"]
                    height = d["height"]
                    csv_fmt = f"{id},{width},{height},{x},{y}\n"
                else:
                    size = d["size"]
                    csv_fmt = f"{id},{size},{x},{y}\n"
                file.write(csv_fmt)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a CSV file"""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                file_lines = file.readlines()
        except FileNotFoundError:
            file_lines = []
        list_dictionaries = []
        for line in file_lines:
            obj_values = line.split(",")
            if cls.__name__ == "Rectangle":
                obj_keys = ["id", "width", "height", "x", "y"]
            else:
                obj_keys = ["id", "size", "x", "y"]
            obj_dict = {
                obj_keys[i]: int(obj_values[i]) for i in range(len(obj_keys))
            }
            list_dictionaries.append(obj_dict)
        return [cls.create(**d) for d in list_dictionaries]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the Rectangles and Squares on Turtle GUI"""
        import turtle

        # Set the shape of the turtle
        papi = turtle.Turtle()
        papi.shape("turtle")

        # Adjust screen and title
        screen = turtle.Screen()
        screen.title("Alx - Rectangles and Squares")

        # Adjust colors
        turtle.colormode(255)
        papi.color(161, 52, 52)
        screen.bgcolor(19, 19, 19)

        # Adjust initial position for Rectangles
        papi.penup()
        papi.setposition(-200, 200)
        papi.pendown()

        # Draw Rectangles
        papi.write("Rectangles: \n", font=("Arial", 20, "bold"))
        max_height = 0
        for rec in list_rectangles:
            width = getattr(rec, "width")
            height = getattr(rec, "height")
            for i in range(2):
                papi.forward(width)
                papi.right(90)
                papi.forward(height)
                papi.right(90)
            if height > max_height:
                max_height = height
            papi.penup()
            papi.forward(width + 20)
            papi.pendown()

        # Adjust initial position for Squares
        papi.penup()
        papi.goto(-200, 200 - max_height - 100)
        papi.setheading(0)
        papi.pendown()

        # Draw Squares
        papi.write("Squares: \n", font=("Arial", 20, "bold"))

        for sqr in list_squares:
            size = getattr(sqr, "size")
            for i in range(4):
                papi.forward(size)
                papi.right(90)
            papi.penup()
            papi.forward(size + 20)
            papi.pendown()

        turtle.done()
