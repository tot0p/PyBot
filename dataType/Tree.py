#-*- coding: utf-8 -*-


class __node:
    def __init__(self,data):
        self.data = data
        self.next_node = []


    def __str__(self):
        return str(self.data) + " children : " + str(self.next_node)


class Tree:

    def __init__(self,data = None)->None:
        if data != None:
            self.root = __node(data)
            self.size = 1
        else:
            self.root = None
            self.size = 0

    def __str__(self)->str:
        return self.__str__(self.root)