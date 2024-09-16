#!/usr/bin/python3

"""
This module defines the 'Square' class.

The 'Square' class represents a square with a private size attribute.
It includes methods to initialize the square with a valid size and
to calculate its area.

The class performs validation to ensure that the size is a non-negative
integer and provides an area calculation method.
"""


class Square:
    """
    A class that defines a square by its size and calculates its area.

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

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size * self.__size
