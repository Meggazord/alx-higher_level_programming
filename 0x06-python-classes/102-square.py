#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square.

    Args:
        size: the size of one side of the square.

    Raises:
        TypeError:  if size is not int
        ValueError: is size is < 0 

    Returns:
        int: area of a square

    """

    def __init__(self, size=0):
        """Initializes a square instance."""

        self.__size = size  # private attribute

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of a square instance."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Returns the size of a square instance."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of a square instance."""
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __eq__(self, other):
        """Equal case."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal case."""
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
