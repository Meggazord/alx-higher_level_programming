#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(c) >= 97 and <= 123:
            c = chr(ord(c) - 32)
            print(f"{c}", end="")
        else:
            print(f"{c:s}", end="")
    print()
