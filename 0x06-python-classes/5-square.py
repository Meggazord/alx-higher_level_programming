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

    def my_print(self):
        """Prints the square."""
        if self.__size == 0:
            print()

        else:
            for _ in range(self.__size):
                print("#" * self.__size)
