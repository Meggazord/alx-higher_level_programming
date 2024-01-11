#!/usr/bin/python3

"""Input / output exercises"""


def append_write(filename="", text=""):
    """Appends a string to the end and returns the number of characters added."""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
