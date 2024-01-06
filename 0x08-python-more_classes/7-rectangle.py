#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle():
    """a rectangle class

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Class Attributes:
    number_of_instances (int): Total number of rectangle instances.
    print_symbol (any): Symbol used for string representation.  

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """object initiation method

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the string representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect_str = ""
            Rectangle.print_symbol = str(self.print_symbol)
            for _ in range(self.__height):
                rect_str += Rectangle.print_symbol * self.__width + "\n"
            return rect_str[:-1]

    def __repr__(self):
        """returns the string representation of a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """deletes a triangle instance"""
        Rectangle.number_of_instances -= 1

        if Rectangle.number_of_instances < 0:
            Rectangle.number_of_instances = 0
        print("Bye rectangle...")
