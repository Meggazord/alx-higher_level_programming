#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 1
    for i in range(3):
        for j in range(3):
            print("{}".format(x), end=" ")
            x += 1
        print()
