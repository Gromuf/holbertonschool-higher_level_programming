#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

BaseGeometry serves as a base class for geometric shapes,
providing an interface for calculating area.
"""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Calculates the area of the shape.

        Raises:
            Exception: If the area method is not implemented in a subclass.
        """
        raise Exception("area is not implemented")
