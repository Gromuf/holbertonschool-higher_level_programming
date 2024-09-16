#!/usr/bin/python3

class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square, kept private.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square (no type/value validation).
        """

        self.__size = size
