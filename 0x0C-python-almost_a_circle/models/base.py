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
