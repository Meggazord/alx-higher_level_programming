#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(c) >= 97 and ord(c) <= 123:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
        else:
            print("{}".format(c), end="")
    print()
