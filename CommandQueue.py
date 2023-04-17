#-*- coding: utf-8 -*-


from dataType.Queue import Queue

from uuid import uuid4

class CommandQueue:

    def __init__(self) -> None:
        self.queue = {}

    def register(self,user:int) -> str:
        '''
        Register a command in the queue by user
        and return a uuid for the command
        '''
        uuid = uuid4().__str__()
        if user in self.queue:
            self.queue[user].push(uuid)
        else:
            self.queue[user] = Queue()
            self.queue[user].push(uuid)
        return uuid

    def wait(self,user:int,uuidCommand:str) -> str:
        '''
        Wait for the command to be executed
        '''
        if user in self.queue:
            if self.queue[user].peek() == uuidCommand:
                return False
            else:
                return True
        else:
            return False
    
    def unregister(self,user:int,uuidCommand:str) -> bool:
        '''
        Unregister a command in the queue by user
        '''
        if user in self.queue:
            if self.queue[user].peek() == uuidCommand:
                self.queue[user].pop()
 