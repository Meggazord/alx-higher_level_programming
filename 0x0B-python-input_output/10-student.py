#!/usr/bin/python3
""" My class module
"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json dictionary creation method"""
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                json_dict[key] = value
        return json_dict
