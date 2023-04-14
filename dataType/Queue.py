#-*- coding: utf-8 -*-

from dataType.Node import Node

class Queue:

    def __init__(self) -> None:
        self.first_node = None

    def push(self, data):
        if self.first_node == None:
            self.first_node = Node(data)
        else:
            currentNode = self.first_node
            while currentNode.next_node != None:
                currentNode = currentNode.next_node
            currentNode.next_node = Node(data)

    def pop(self):
        if self.first_node == None:
            return None
        else:
            data = self.first_node.data
            self.first_node = self.first_node.next_node
            return data
        
    def peek(self):
        if self.first_node == None:
            return None
        else:
            return self.first_node.data
    

    def __len__(self) -> int:
        if self.first_node == None:
            return 0
        else:
            currentNode = self.first_node
            size = 1
            while currentNode.next_node != None:
                currentNode = currentNode.next_node
                size += 1
            return size
        
    def size(self):
        return len(self)

    def __str__(self) -> str:
        currentNode = self.first_node
        string = ""
        while currentNode.next_node != None:
            string += str(currentNode.data)+"\n"
            currentNode = currentNode.next_node
        string += str(currentNode.data)
        return string