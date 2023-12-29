#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square.

    Args:
        size (int): the size of one side of the square.
        position (tuple): the position of a square


    Raises:
        TypeError:  if size is not int or if position is not a tuple of 2 positive integers
        ValueError: is size is < 0

    Returns:
        int: area of a square

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance and its position."""
        self.__size = size  # private attribute
        self.position = position

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

    @property
    def position(self):
        """Returns the position of a square instance."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of a square instance."""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(v, int) for v in value) \
                or not all(v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints the square and its position."""
        if self.__size == 0:
            print()

        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(self.__position[0] * " ", end="")
                print("#" * self.__size)

    def __str__(self):
        """String representation of the Square instance."""
        result = ""
        if self.__size == 0:
            return result
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0]
                result += "#" * self.__size
                if _ != self.__size - 1:
                    result += "\n"
        return (result)
