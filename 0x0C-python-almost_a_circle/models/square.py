#!/usr/bin/python3

""" Module containing the Square class """

from rectangle import Rectangle


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

    def to_dictionary(self):
        """returns dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

        def to_csv_row(self):
            """returns Square CSV representation"""
            return [self.id, self.width, self.x, self.y]

        @staticmethod
        def create_from_csv_row(row):
            """"creates Square CSV representation"""
            return Square(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
