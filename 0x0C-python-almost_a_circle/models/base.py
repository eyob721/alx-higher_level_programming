#!/usr/bin/python3
"""This module contains the Base class."""


class Base:
    """Class definition of the Base.
    This class will be the base of all other classes in the project.

    Attributes:
        id (int): Id the object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class

        Note:
            Type of id is not checked, it is assumed to be an integer.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts Python list of dictionaries to JSON String

        Args:
            list_dictionaries (list): List of  dictionaries

        Returns:
            If the list is empty or None, it returns '[]', otherwise it
            returns the JSON string representation of `list_dictionaries`.

        """
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to Python list.

        Args:
            json_string: JSON String Representation of list of dictionaries.

        Returns:
            List of dictionaries

        """
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of objects to a file

        Args:
            list_objs (list): List of objects that inherit from Base.

        """
        file_name = cls.__name__ + ".json"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(file_name, "w", encoding="utf-8") as file:
            json_string = cls.to_json_string(list_dictionaries)
            file.write(json_string + '\n')

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read().rstrip('\n'))
        except FileNotFoundError:
            list_dicts = []
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj
