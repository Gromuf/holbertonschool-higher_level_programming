#!/usr/bin/python3
"""
This module provides a function to return a list of attributes
and methods for an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of attribute and method names.
    """
    return (dir(obj))
