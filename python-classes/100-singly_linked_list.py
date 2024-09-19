#!/usr/bin/python3

"""
This module defines two classes: Node and SinglyLinkedList.

The Node class represents a node in a singly linked list, with data and
a pointer to the next node.

The SinglyLinkedList class defines a singly linked list with operations
to insert nodes in sorted order and print the entire list.

The module ensures that data in each node is an integer, and that
next_node is either None or another Node instance.
"""


class Node:
    """
    Defines a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node. Must be an integer.
        next_node (Node): The next node in the list, or None.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node with data and an optional next_node.

        Args:
            data (int): The data for the node.
            next_node (Node): The next node in the linked list (default: None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data for the node. Must be an integer.

        Args:
            value (int): The data to set.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node.

        Returns:
            Node: The next node in the list or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node. Must be a Node object or None.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("value must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.

    Attributes:
        __head (Node): The head node of the list (private).
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Prints the entire list as a string, one node per line.

        Returns:
            str: The string representation of the linked list.
        """
        current_node = self.__head
        res = []
        while current_node is not None:
            res.append(str(current_node.data))
            current_node = current_node.next_node
        return "\n".join(res)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the list in increasing order.

        Args:
            value (int): The data value to be inserted into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None
                   and current_node.next_node.data < value):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node
