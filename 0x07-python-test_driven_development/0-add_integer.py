#!/usr/bin/python3

"""addtion module"""


def add_integer(a, b=98):
    """adds 2 integers"""
    if a is None or (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

"""
try:
    add_integer(None)
except TypeError as e:
    print(f"{e}")

add_integer(float('nan'), 2) """
