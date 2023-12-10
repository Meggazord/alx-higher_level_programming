#!/usr/bin/python3
with open('add_0.py', 'r') as file:
    code = file.read()

exec(code)

a = 1
b = 2

add = locals()['add']

result = add(a, b)
print(f"{a} + {b} = {result}")
