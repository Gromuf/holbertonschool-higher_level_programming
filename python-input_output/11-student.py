#!/usr/bin/python3
"""
Module defines a class Student with attributes first name, last name, and age.
It includes methods for JSON serialization and reloading instance attributes.
"""


class Student:
    """
    Represents a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the instance.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: Dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        return {
            attr: getattr(self, attr)
            for attr in attrs if attr in self.__dict__
        }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the instance using the json dictionary.

        Args:
            json (dict): A dictionary of new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
