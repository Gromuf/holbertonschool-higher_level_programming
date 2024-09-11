#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a
given number.

The function `matrix_divided` takes a matrix (a list of lists of integers
or floats) and divides each element by a specified divisor. The result is
a new matrix where each element is rounded to 2 decimal places.

Functions:
- matrix_divided(matrix, div): Divides all elements of the matrix by the
  divisor and returns a new matrix.

Exceptions:
- TypeError: Raised if the matrix is not a list of lists of integers or
  floats, or if the divisor is not a number.
- ZeroDivisionError: Raised if the divisor is zero.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number
    and rounds the result to 2 decimal places.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The divisor for the division.

    Returns:
    list of lists of float: A new matrix with all elements divided by div,
    rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats.
    TypeError: If any row of the matrix is not the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is zero.
    """
    if (
        not isinstance(matrix, list)
        or not all(isinstance(row, list) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not all(
        isinstance(elem, (int, float)) for row in matrix for elem in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of a matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
