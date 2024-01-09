#!/usr/bin/python3
"""
Module for problem solving
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """object initialization method"""
        self.__size = self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns the value of the area"""
        return self.__size ** 2

    def __str__(self):
        """returns the str rep of the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
