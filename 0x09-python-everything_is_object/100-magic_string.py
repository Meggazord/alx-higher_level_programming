#!/usr/bin/python3
def magic_string(a=[1]):
    return "BestSchool" * a[0]
    a[0] += 1


for i in range(10):
    print(magic_string())
