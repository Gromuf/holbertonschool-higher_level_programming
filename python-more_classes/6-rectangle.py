#!/usr/bin/python3

"""
Module for defining a rectangle.

This module provides the Rectangle class, which represents a rectangle
with private attributes for width and height. It includes methods for
getting and setting these attributes, calculating the area and perimeter,
printing the rectangle using the '#' character, and providing a `repr()`
method for recreating the instance.
"""


class Rectangle:
    """A class that defines a rectangle.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or
            height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for _ in range(self.height):
            rectangle += "#" * self.width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle.

        This string is formatted as a valid Python expression that can
        be used to recreate the instance using `eval()`.

        Returns:
            str: A string representation of the rectangle.
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
