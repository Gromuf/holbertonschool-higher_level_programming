#!/usr/bin/python3
"""
This module provides a function to write a string to a UTF-8 encoded text file.

The function `write_file` writes a given text to a specified file, creating
the file if it doesn't exist and overwriting its content if it does. The
function returns the number of characters written to the file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
