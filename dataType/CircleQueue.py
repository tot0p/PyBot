#-*- coding: utf-8 -*-

from dataType.Node import Node

class CircleQueue:


    def __init__(self) -> None:
        self.first_node = None

    def push(self, data):
        if self.first_node == None:
            self.first_node = Node(data)
            self.first_node.next_node = self.first_node
        else:
            currentNode = self.first_node
            while currentNode.next_node != self.first_node:
                currentNode = currentNode.next_node
            currentNode.next_node = Node(data)
            currentNode.next_node.next_node = self.first_node


    def pop(self):
        if self.first_node == None:
            return None
        else:
            data = self.first_node.data
            self.first_node = self.first_node.next_node
            self.push(data)
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
            while currentNode.next_node != self.first_node:
                currentNode = currentNode.next_node
                size += 1
            return size
        
    def size(self):
        return len(self)