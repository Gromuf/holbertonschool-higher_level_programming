#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""
This module defines an abstract class Animal and its subclasses Dog
and Cat. The Animal class requires subclasses to implement a sound
method that returns the specific sound of the animal.
"""


class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """Dog class that implements the Animal abstract class."""
    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Cat class that implements the Animal abstract class."""
    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
