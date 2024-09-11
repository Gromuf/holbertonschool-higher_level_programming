#!/usr/bin/python3

"""
4-print_square

This module provides a function to print a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
    size (int): The size of the square.

    Raises:
    TypeError: If size is not an integer or if size is a float and less than 0.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
