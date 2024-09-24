#!/usr/bin/env python3
"""
This module demonstrates the use of mixins to compose behaviors in classes.
The Dragon class inherits both swimming and flying abilities from SwimMixin
and FlyMixin, respectively. The Dragon class also has its own roar behavior.
"""


class SwimMixin:
    """A mixin to add swimming behavior."""

    def swim(self):
        """Prints a message indicating the creature is swimming."""
        print("The creature swims")


class FlyMixin:
    """A mixin to add flying behavior."""

    def fly(self):
        """Prints a message indicating the creature is flying."""
        print("The creature flies")


class Dragon(SwimMixin, FlyMixin):
    """Represents a Dragon that can swim, fly, and roar."""

    def roar(self):
        """Prints a message indicating the dragon is roaring."""
        print("The dragon roars!")
