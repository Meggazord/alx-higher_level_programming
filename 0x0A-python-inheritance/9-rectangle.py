#!/usr/bin/python3
"""
Module for problem solving
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """object initialization method"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """returns the value of the area"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
