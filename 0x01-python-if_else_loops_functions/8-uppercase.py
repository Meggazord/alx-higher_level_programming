#!/usr/bin/python3
def uppercase(str):
    up_string = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        up_string += i
    print("{}".format(up_string))
