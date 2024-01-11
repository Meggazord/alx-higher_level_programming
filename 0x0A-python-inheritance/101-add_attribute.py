#!/usr/bin/python3
"""
This is a class

A class representing a rebel integer inheriting int.
It inverts the behavior of the equality and inequality operators.
"""

def add_attribute(obj, attribute, value):
    """Add attribute to object if possible, otherwise raise TypeError"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
