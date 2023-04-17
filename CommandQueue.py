#-*- coding: utf-8 -*-


from dataType.Queue import Queue

from uuid import uuid4

class CommandQueue:


    def __init__(self) -> None:
        self.queue = {}


    def register(self,user:int) -> str:
        uuid = uuid4().__str__()
        if user in self.queue:
            self.queue[user].push(uuid)
        else:
            self.queue[user] = Queue()
            self.queue[user].push(uuid)
        return uuid

    def wait(self,user:int,uuidCommand:str) -> str:
        if user in self.queue:
            if self.queue[user].peek() == uuidCommand:
                self.queue[user].pop()
                return False
            else:
                return True
        else:
            return False
    
