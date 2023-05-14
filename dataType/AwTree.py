#-*- coding: utf-8 -*-

import json

class node :
    '''
    A node that can be used to ask questions and get responses.
    '''

    question : None | str
    responses : None | list
    next_nodes : list

    def __init__(self, question : None | str = None, responses : None | list = None) -> None:
        self.question = question
        self.responses = responses
        self.next_nodes = []


    def __str__(self) -> str:
        return self.question if self.question != None else 'None'
    
    def delete(self,question : str) -> None:
        '''
        Delete a node from the tree.
        '''
        for node in self.next_nodes:
            if node.question == question:
                self.next_nodes.remove(node)
                return
            else:
                node.delete(question)

    def append(self,question : str, responses : list, previous_question : str) -> None:
        '''
        Append a new node to the tree.
        '''
        if self.question == previous_question:
            self.next_nodes.append(node(question,responses))
        else:
            for Node in self.next_nodes:
                Node.append(question,responses,previous_question)


    def load(self,data : dict) -> None:
        '''
        Load a tree from a json file.
        '''
        if "question"  in data:
            self.question = data['question']
        if "responses" in data:
            self.responses = data['responses']
        if "next_nodes" in data:
            for Node in data['next_nodes']:
                question = None if 'question' not in Node else Node['question']
                responses = None if 'responses' not in Node else Node['responses']
                self.next_nodes.append(node(question,responses))
                self.next_nodes[-1].load(Node)

class AwTree:
    '''
    A tree that can be used to ask questions and get responses.
    '''

    root : node | None
    current_node : node | None

    def __init__(self, question : None | str = None) -> None:
        self.root = node(question)
        self.current_node = self.root

    def __str__(self) -> str:
        return self.current_node.__str__()
    
    def append(self,question : str, responses : list, previous_question : str) -> None:
        '''
        Append a new node to the tree.
        '''
        self.root.append(question,responses,previous_question)


    def delete(self,question : str) -> None:
        '''
        Delete a node from the tree.
        '''
        if self.root.question == question:
            self.root = None
        self.root.delete(question)
        if self.current_node.question == question:
            self.current_node = self.root


    def get_question(self) -> str:
        '''
        Get the current question.
        '''
        return self.current_node.question
    
    def is_end(self) -> bool:
        '''
        Check if the current node is a leaf.
        '''
        return self.current_node.next_nodes == []
    
    def send_answer(self,answer : str) -> bool:
        '''
        Send an answer to the current question.
        '''
        answer = answer.lower()
        for node in self.current_node.next_nodes:
            if answer in node.responses:
                self.current_node = node
                return True
        return False

    def load(self,file : str) -> None:
        '''
        Load a tree from a json file.
        '''
        with open(file,'r') as f:
            data = json.load(f)
        self.root.load(data)


    def loadJson(self,json : str) -> None:
        '''
        Load a tree from a json string.
        '''
        self.root.load(json)

    def printAllTree(self) -> None:
        '''
        Print the tree.
        '''
        str = self.root.question
        for node in self.root.next_nodes:
            str += node.question
        print(str)


   

if __name__ == "__main__":

    test = AwTree()


    test.load('../data/AwTree.json')
    test.printAllTree()


# json file
