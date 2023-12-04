#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = [tuple_a[0] if len(tuple_a) > 0 else 0,
              tuple_a[1] if len(tuple_a) > 1 else 0]
    list_b = [tuple_b[0] if len(tuple_b) > 0 else 0,
              tuple_b[1] if len(tuple_b) > 1 else 0]

    new_tuple = (list_a[0] + list_b[0], list_a[1] + list_b[1])
    return new_tuple
