#!/usr/bin/python3

""" Module containing the Base class """

import json
import csv


class Base:
    """ Base class for managing id attribute """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as file:
            file.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(1, 1, 0, 0)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_string = file.read()
                list_of_dict = Base.from_json_string(json_string)
                return [cls.create(**s) for s in list_of_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """method to serialize to a CSV"""
        if list_objs is None or len(list_objs) == 0:
            return
        else:
            file_name = cls.__name__ + ".csv"
            with open(file_name, mode="w", newline='') as file:
                writer = csv.writer(file)
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """method to deserialize from a CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                return [cls.create_from_csv_row(row) for row in reader]
        except FileNotFoundError:
            return []
