#!/usr/bin/python3
"""
This module defines a function `inherits_from` that checks if an
object is an instance of a class that inherited (directly or indirectly)
from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    from a_class (directly or indirectly).

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or any subclass
              of a_class, but not if it is an instance of a_class
              itself. Returns False otherwise.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
