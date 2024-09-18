#!/usr/bin/python3

"""
This module defines the 'Square' class.

The 'Square' class represents a square with private size and position
attributes. It includes methods for validating these attributes,
calculating the area of the square, and printing a visual representation
of the square.
"""


class Square:
    """A class that defines a square by its size and calculates its area."""

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
        """Retrieves the size of the square."""
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
        """Retrieves the position of the square."""
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
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""

        return self.__size ** 2

    def my_print(self):
        """
        Print a visual representation of the square using '#' characters.

        If the size is 0, an empty line is printed. The square is printed with
        offset positions specified by __position.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
