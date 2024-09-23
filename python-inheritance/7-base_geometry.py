#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

BaseGeometry serves as a base class for geometric shapes,
providing an interface for calculating area and validating integers.
"""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Calculates the area of the shape.

        Raises:
            Exception: If the area method is not implemented in a subclass.
        """
        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
