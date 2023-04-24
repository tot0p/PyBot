#-*- coding: utf-8 -*-


from uuid import uuid4

from dataType.Queue import Queue

class AccessHistorique:
    def __init__(self):
        self.queue = Queue()

    def lock(self):
        uuid = uuid4().__str__()
        self.queue.push(uuid)
        return uuid
    
    def wait(self,uuid):
        while self.queue.peek() != uuid:
            pass

    def unlock(self,uuid):
        if self.queue.peek() == uuid:
            self.queue.pop()
            return True
        return False