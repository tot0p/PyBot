from dataType.Node import Node

class ListChained:
  def __init__(self, first_data):
    self.firstNode = Node(first_data) 
    self.lastNode = self.firstNode
    self.size = 1

  def append(self,data):
    self.lastNode.NextNode = Node(data)
    self.lastNode = self.lastNode.NextNode
    self.size +=1

  def insert_first(self,data):
    currentNode = Node(data)
    currentNode.NextNode = self.firstNode
    self.firstNode =currentNode
    self.size +=1

  def size(self):
    return self.size

  def insert(self, indice, data):
    currentNode = self.firstNode
    i = 0
    while indice > i:
      currentNode = currentNode.NextNode
      i += 1
    newNode = Node(data)
    newNode.NextNode = currentNode.NextNode
    currentNode.NextNode = newNode

    self.size += 1
  
  def __str__(self) -> str:
    currentNode = self.firstNode
    string = ""
    while currentNode.NextNode != None:
      string += str(currentNode.data)+" "
      currentNode = currentNode.NextNode
    string += str(currentNode.data)
    return string

# class Node:
#   def __init__(self,data):
#     self.data = data
#     self.NextNode = None
#     self.PrevNode = None