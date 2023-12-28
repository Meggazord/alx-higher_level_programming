#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square.

    Args:
        size: the size of one side of the square.

    Raises:
        TypeError:  if size is not int
        ValueError: is size is < 0 

    """

    def __init__(self, size=0):
        """Initializes a square instance."""
        self.__size = size  # private attribute

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
