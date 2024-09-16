#!/usr/bin/python3

"""
This module defines the 'Square' class.

The 'Square' class represents a square with private size and position
attributes. It includes methods for validating these attributes,
calculating the area of the square, and printing a visual representation
of the square.
"""


class Square:
    """
    A class that defines a square by its size and calculates its area.

    Attributes:
        __size (int): The size of the square, kept private.
        __position (tuple): The position of the square, kept private.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.

        Args:
            size (int, optional): The size of the square. Must be non-negative.
            Default is 0.
            position (tuple, optional): The position of the square. Must be
            a tuple of two non-negative integers. Default is (0, 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of two positive integers.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): The position of the square. Must be a tuple of two
            non-negative integers.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 integers")
        self.__position = value

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

        If size is 0, prints an empty line.
        Position is used to space the square horizontally and vertically.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
