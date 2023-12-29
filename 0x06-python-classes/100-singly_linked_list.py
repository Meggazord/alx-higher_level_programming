#!/usr/bin/python3
"""Defines a class of a Singly Linked List.

A singly linked list is a list which is singly linked. 

"""


class Node:
    """Node class."""

    def __init__(self, data, next_node=None):
        """Node inititation."""
        self.data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Returns the value of data in a Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the value of data in a Node."""
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Returns the value of the next Node."""
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Creates the next Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class."""

    def __init__(self):
        """Singly Linked List inititation."""
        self.head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list (increasing order)"""
        new_node = Node(value)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation of the Singly Linked List."""
        result = ""

        current = self.head

        while (current):
            if current.next_node is None:
                result += str(current.data)
            else:
                result += str(current.data) + "\n"
            current = current.next_node

        return (result)


sll = SinglyLinkedList()
sll.sorted_insert(2)
print(sll)
