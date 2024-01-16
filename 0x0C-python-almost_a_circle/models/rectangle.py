#!/usr/bin/python3

""" Module containing the Rectangle class """
import sys
sys.path.append(
    '/Users/Megahed/alx/projects/alx-higher_level_programming/0x0C-python-almost_a_circle/')

from models.base import Base


class Rectangle(Base):
    """Rectangle class which inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints the Rectangle instance with the character #"""
        for i in range(self.x):
            print()
        for i in range(self.height):
            print(self.y * " " + self.width * '#')

    def __str__(self):
        """returns Rectangle dimensions"""
        return "[Rectangle] ({}) <{}>/<{}> - <{}>/<{}>".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def to_csv_row(self):
        """returns Square CSV representation"""
        return [self.id, self.width, self.height, self.x, self.y]

    @staticmethod
    def create_from_csv_row(row):
        """"creates Rectangle CSV representation"""
        return Rectangle(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
