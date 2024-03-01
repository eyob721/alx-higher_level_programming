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
            file.write(json_string)
