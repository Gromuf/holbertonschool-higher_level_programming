#!/usr/bin/python3
"""
This module provides a function to create an object from a JSON file
using the built-in `json` library.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file from which to load the JSON data.

    Returns:
        object: The Python object represented by the JSON data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
