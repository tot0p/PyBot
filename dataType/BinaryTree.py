#-*- coding: utf-8 -*-


class __TreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data) + " fl " + str(self.left) + " fd " + str(self.right)
    

    def __len__(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return 1 + len(self.right)
        elif self.right == None:
            return 1 + len(self.left)
        else:
            return 1 + len(self.left) + len(self.right)
        

    def append(self,data):
        if data > self.data:
            if self.right == None:
                self.right = __TreeNode(data)
            else:
                self.right.append(data)
        else:
            if self.left == None:
                self.left = __TreeNode(data)
            else:
                self.left.append(data)
        

    def __iter__(self):
        if self.left == None and self.right == None:
            yield self.data
        elif self.left == None:
            yield self.data
            for i in self.right:
                yield i
        elif self.right == None:
            yield self.data
            for i in self.left:
                yield i
        else:
            yield self.data
            for i in self.left:
                yield i
            for i in self.right:
                yield i



class BinaryTree:
    def __init__(self,data=None):
        if data == None:
            self.root = None
        else:
            self.root = __TreeNode(data)

    def append(self,data):
        if self.root == None:
            self.root = __TreeNode(data)
        else:
            self.root.append(data)


    def __str__(self):
        return str(self.root)
    
    def __len__(self):
        return len(self.root)
    
    def __iter__(self):
        return self.root.__iter__()

    

if __name__ == "__main__":

    tree = BinaryTree(1)
    tree.append(1)
    tree.append(2)
    tree.append(3)
    tree.append(4)
    tree.append(-1)

    print(tree)

    for i in tree:
        print(i)
