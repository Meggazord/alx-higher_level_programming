#!/usr/bin/python3

class MyInt(int):
    """
    A class representing a rebel integer inheriting from int.
    It inverts the behavior of the equality and inequality operators.
    """

    def __eq__(self, other):
        """Override the equality operator."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override the inequality operator."""
        return not super().__ne__(other)
