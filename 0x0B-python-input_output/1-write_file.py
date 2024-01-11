#!/usr/bin/python3

"""Input / output exercises"""


def write_file(filename="", text=""):
    """ function to write to files"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
