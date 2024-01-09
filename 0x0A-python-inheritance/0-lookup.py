#!/usr/bin/python3
"""
The module of the lookup function
"""


def lookup(obj)
    """"
    Return all attributes and methods in the object's class.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing all the attributes and methods in the class of the object.
    """
    return dir(obj)
