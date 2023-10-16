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
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
