#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, element in enumerate(i):
            if j != 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print()
