#-*- coding: utf-8 -*-


from dataType.Node import Node

class ListChained:
    def __init__(self, first_data):
        self.firstNode = Node(first_data) 
        self.size = 1

    def __str__(self) -> str:
        currentNode = self.firstNode
        string = ""
        while currentNode.NextNode != None:
            string += str(currentNode.data)+" "
            currentNode = currentNode.NextNode
        string += str(currentNode.data)
        return string

    def append(self,data):
        '''
        append data to the list was sorted
        '''
        currentNode = self.firstNode
        previousNode = None
        while currentNode != None and currentNode.data < data:
            previousNode = currentNode
            currentNode = currentNode.NextNode
        newNode = Node(data)
        if previousNode == None:
            newNode.NextNode = self.firstNode
            self.firstNode = newNode
        else:
            newNode.NextNode = currentNode
            previousNode.NextNode = newNode

        self.size += 1


def test():
    list = ListChained(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.append(6)
    list.append(7)
    list.append(8)
    list.append(3)
    print(list)