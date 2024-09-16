#!/usr/bin/python3

"""
This module defines the 'Square' class.

The 'Square' class represents a square with a private size attribute.
It includes methods for validating the size, retrieving and setting it
through properties, calculating the area of the square, and printing
a visual representation of the square.
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
            size (int, optional): The size of the square. Must be non-negative.
            Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size of the square. Must be non-negative.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square, computed as size * size.
        """

        return self.__size * self.__size

    def my_print(self):
        """
        Prints a visual representation of the square using '#' characters.

        If the size is 0, prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
