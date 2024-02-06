#!/usr/bin/python3
"""Task 7"""


class Node:
    """Class definition for a Node"""

    def __init__(self, data, next_node=None):
        """Node constructor

        Args:
            data: Integer data of the node.
            next_node: Reference to the next node. Defaults to None.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Reference to the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Class definition for a Singly linked list object"""

    def __init__(self):
        """Singly linked list constructor"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the correct sorted order in the list.

        Args:
            value (:obj): A value for the new node.

        """
        n = Node(value)
        prev = cur = self.__head

        while cur is not None and n.data > cur.data:
            prev = cur
            cur = cur.next_node
        n.next_node = cur
        if cur == self.__head:
            self.__head = n
        elif prev is not None:
            prev.next_node = n

    def __str__(self):
        """String representation of Singly linked list object"""
        list_str = ""
        cur = self.__head
        while cur is not None:
            list_str += str(cur.data)
            cur = cur.next_node
            if cur is not None:
                list_str += "\n"
        return list_str
