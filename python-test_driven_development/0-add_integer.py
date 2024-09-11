#!/usr/bin/python3

"""
This module provides a function to add two integers or
floats after converting them to integers.

The `add_integer` function takes two parameters, `a` and `b`,
which can be integers or floats.
The function casts these parameters to integers
and returns their sum. If the parameters are not of type integer or float,
a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after converting them to integers.

    Parameters:
    a: The first number (int or float).
    b: The second number (int or float), defaults to 98.

    Returns:
    The sum of a and b as an integer.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
