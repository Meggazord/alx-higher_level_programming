#!/usr/bin/python3
for i in range(90, 64, -1):
    print("{}".format(chr(i + (i % 2) * 32)), end="")
