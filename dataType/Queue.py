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
            while currentNode.NextNode != None:
                currentNode = currentNode.NextNode
            currentNode.NextNode = Node(data)

    def pop(self):
        if self.first_node == None:
            return None
        else:
            data = self.first_node.data
            self.first_node = self.first_node.NextNode
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
            while currentNode.NextNode != None:
                currentNode = currentNode.NextNode
                size += 1
            return size
        
    def size(self):
        return len(self)

    def __str__(self) -> str:
        currentNode = self.first_node
        if currentNode == None:
            return "None"
        string = ""
        while currentNode.NextNode != None:
            string += str(currentNode.data)+"\n"
            currentNode = currentNode.NextNode
        string += str(currentNode.data)
        return string
    

    def IsEmpty(self):
        return self.first_node == None