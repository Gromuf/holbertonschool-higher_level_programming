#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []

    for i in matrix:
        square_i = []

        for element in i:
            square_i.append(element ** 2)

        square_matrix.append(square_i)

    return square_matrix
