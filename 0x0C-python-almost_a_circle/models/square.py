#!/usr/bin/python3

""" Module containing the Square class """
import sys
sys.path.append(
    '/Users/Megahed/alx/projects/alx-higher_level_programming/0x0C-python-almost_a_circle')

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class which inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """returns Square dimensions"""
        return "[Square] ({}) <{}>/<{}> - <{}>".format(self.id, self.x, self.y, self.width)
