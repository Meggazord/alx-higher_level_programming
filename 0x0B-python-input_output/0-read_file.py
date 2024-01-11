#!/usr/bin/python3

"""Input / output exercises"""


def read_file(filename=""):
    """ function to read files"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.readline())
