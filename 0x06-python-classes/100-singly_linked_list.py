#!/usr/bin/python3
"""A module for Task 7."""


class Node:
    """A class definition for the Node object.

    Args:
        data (int): Intger data of the node.
        next_node (Node | None): Reference to the next node. Defaults to None.

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A class definition for the Singly linked list object."""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted order in the list.

        Args:
            value (:obj): A value for the new node.

        Returns:
            None

        """
        n = Node(value)
        prev = cur = self.__head

        while cur is not None and n.data > cur.data:
            prev = cur
            cur = cur.next_node
        n.next_node = cur
        if cur == self.__head:
            self.__head = n
        else:
            prev.next_node = n

    def __str__(self):
        list_str = ""
        cur = self.__head
        while cur is not None:
            list_str += str(cur.data)
            cur = cur.next_node
            if cur is not None:
                list_str += '\n'
        return list_str
