#!/usr/bin/python3
"""
This module defines the Square class, which inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square that inherits from Rectangle."""
    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square (length of one side).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
