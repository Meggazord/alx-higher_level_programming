#!/usr/bin/python3
""" My class module
"""


def class_to_json(obj):
    """Returns a dictionary description for JSON serialization of an object."""
    json_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
