from dataType.Node import Node

class Stack:
    def __init__(self, first_data):
        self.lastNode = Node(first_data) 
        self.size = 1

    def __str__(self) -> str:
        currentNode = self.lastNode
        string = "["
        while currentNode.NextNode != None:
            string += str(currentNode.data)+","
            currentNode = currentNode.NextNode
        string += str(currentNode.data)
        return string + "]"

    def push(self,data):
        currentNode = self.lastNode
        while currentNode.NextNode != None:
            currentNode = currentNode.NextNode
        currentNode.NextNode = Node(data)
        self.size += 1

    def pop(self):
        currentNode = self.lastNode
        while currentNode.NextNode.NextNode != None:
            currentNode = currentNode.NextNode
        temp = currentNode.NextNode
        currentNode.NextNode = None
        self.size -= 1
        return temp.data
    
    def peek(self):
        currentNode = self.lastNode
        while currentNode.NextNode != None:
            currentNode = currentNode.NextNode
        return currentNode.data
    
    def size(self):
        return self.size