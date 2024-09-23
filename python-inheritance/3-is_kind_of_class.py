#!/usr/bin/python3
"""
This module defines a function `is_kind_of_class` that checks if an object
is an instance of a specified class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or its subclasses.
    """
    return isinstance(obj, a_class)
