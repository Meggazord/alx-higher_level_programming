#!/usr/bin/python3
"""
Module for problem solving

This module provides a function 'lookup' to inspect objects and retrieve a list of all attributes and methods
belonging to their class.
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
