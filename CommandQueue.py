#-*- coding: utf-8 -*-


from dataType.Queue import Queue

class CommandQueue:


    def __init__(self) -> None:
        self.queue = {}


    def register(self,command,user) -> int:
        if user in self.queue:
            self.queue[user].push(command)
        else:
            self.queue[user] = Queue()
            self.queue[user].push(command)
        return len(self.queue[user])

    
