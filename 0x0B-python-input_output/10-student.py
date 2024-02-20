#!/usr/bin/python3
"""Task 10"""


class Student:
    """Class definition of Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Retrieves a dictionary representation of a Student"""
        obj_dict = self.__dict__
        if type(attr) is not list:
            return obj_dict
        for a in attr:
            if type(a) is not str:
                return obj_dict
        return {a: obj_dict[a] for a in obj_dict if a in attr}
