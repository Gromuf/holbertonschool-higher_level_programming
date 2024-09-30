#!/usr/bin/python3
"""
This module provides a function to append a string to a UTF-8 encoded text file

The function `append_write` appends a given text to the end of a specified file
creating the file if it doesn't exist. It returns the number of characters
added to the file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of
    characters added.

    Args:
        filename (str): The name of the file to append to.
                        Defaults to an empty string if not provided.
        text (str): The string to append to the file.
                    Defaults to an empty string if not provided.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
