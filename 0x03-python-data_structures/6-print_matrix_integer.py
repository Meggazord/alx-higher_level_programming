#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        for i, num in enumerate(row):
            if i != len(row) - 1:
                print("{}".format(num), end=" ")
            else:
                print("{}".format(num))
    return
