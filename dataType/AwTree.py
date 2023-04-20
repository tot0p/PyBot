#-*- coding: utf-8 -*-

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
    
    def send_answer(self,answer : str) -> bool:
        '''
        Send an answer to the current question.
        '''
        for node in self.current_node.next_nodes:
            if answer in node.responses:
                self.current_node = node
                return True
        return False


if __name__ == "__main__":

    test = AwTree('Is it a dog?')
    test.append('Is it a cat?',['Yes','No'],'Is it a dog?')
    test.append('Is it a dog?',['Yes','No'],'Is it a cat?')


    print(test.get_question())
    print(test.send_answer('Yes'))
    print(test.get_question())
    print(test.send_answer('Yes'))