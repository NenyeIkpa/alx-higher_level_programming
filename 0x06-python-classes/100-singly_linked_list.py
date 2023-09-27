#!/usr/bin/python3

"""creates a Node class for a singly linked list"""
class Node:
    """defining properties and methods of the Node class"""

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
        if type(value) is not None or type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @data.setter
    def data(self, value):
        """sets the value of private property, data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
        
    def __init__(self, data, next_node=None):
        """initializes a node object"""
        self.__data = data
        self.__next_node = next_node
        

class SinglyLinkedList:
    """mapping out attributes of the SinglyLinkedList class"""

    def __init__(self):
        """initializes a singly linked list"""
        self.__head = Node(0, None)

    def sorted_insert(self, value):
        if self.__head.data == 0 and self.__head.next_node == None:
            self.__head == Node(value, None)
        elif value < self.__head.data:
            new_node = Node(value, self.__head);
            self.__head = new_node
        else:
            looper = self.__head
            while looper != None:
                if looper.data < value:
                    looper = looper.next_node
                else:
                    new_node = Node(value, looper.next_node);
                    looper.next_node = new_node
                    break

