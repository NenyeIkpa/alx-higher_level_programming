#!/usr/bin/python3

"""creates a Node class for a singly linked list"""


class Node:
    """defining properties and methods of the Node class"""

    def __init__(self, data, next_node=None):
        """initializes a node object"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if type(next_node) is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """returns value of private property, data"""
        return self.__data

    @property
    def next_node(self):
        """returns the value of private property, next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the value of private property, next_node"""
        if type(value) is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @data.setter
    def data(self, value):
        """sets the value of private property, data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value


class SinglyLinkedList:
    """mapping out attributes of the SinglyLinkedList class"""

    def __init__(self):
        """initializes a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.__next_node = self.__head
            self.__head = new_node
        else:
            looper = self.__head
            while looper.next_node is not None:
                if looper.__data < value:
                    looper = looper.__next_node
                else:
                    new_node.__next_node = looper.__next_node
                    looper.__next_node = new_node

    def __str__(self):
        """ i ain't sure what is going on here"""
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
