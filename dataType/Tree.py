#-*- coding: utf-8 -*-


class __node:
    def __init__(self,data):
        self.data = data
        self.next_node = []


    def __len__(self):
        count = 1
        for node in self.next_node:
            count += len(node)
        return count

    def __str__(self):
        return str(self.data) + " children : " + str(self.next_node)
    
    def search(self,data):
        if self.data == data:
            return True
        else:
            for child in self.next_node:
                result =  child.search(data)
                if result:
                    return True
            return False


class Tree:

    def __init__(self,data = None)->None:
        if data != None:
            self.root = __node(data)
        else:
            self.root = None

    def __str__(self)->str:
        return self.root.__str__()
    
    def __len__(self)->int:
        return self.root.__len__()
    

    def search(self,data):
        if self.root == None:
            return False
        else:
            return self.root.search(data)
        

if __name__ == "__main__":
    tree = Tree()
    tree.root = __node(1)
    tree.root.next_node.append(__node(2))
    tree.root.next_node.append(__node(3))

    print(tree)

    print(tree.search(3))

    print(tree.search(4))