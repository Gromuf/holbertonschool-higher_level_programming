#!/usr/bin/env python3
"""
Module for a verbose list that provides notifications
when items are added or removed.

The VerboseList class extends the built-in list class,
overriding methods to include print statements that notify
the user of changes to the list.
"""


class VerboseList(list):
    """A list that provides verbose notifications on modifications."""

    def append(self, item):
        """Append an item to the list and notify."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extend the list with items from an iterable and notify."""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Remove an item from the list and notify."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and notify."""
        try:
            print("Popped [{}] from the list.".format(self[index]))
            return super().pop(index)
        except IndexError:
            print("Index out of range. Cannot pop from the list.")
