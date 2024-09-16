#!/usr/bin/python3

"""
This module defines the 'Square' class.

The 'Square' class defines a square with a private size attribute
and ensures proper validation of the size.
"""

class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square, kept private.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square (must be an integer >= 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
