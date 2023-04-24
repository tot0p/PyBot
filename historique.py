#-*- coding: utf-8 -*-

from dataType.ListChained import ListChained
from dataType.Queue import Queue

import time

from constant import HISTORY_JSON

import json
import os

from tools import CustomJsonCoder 


from uuid import uuid4


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
    


class Historique:
    def __init__(self):
        self.all_historique = {} 
        self.access = AccessHistorique()
        self.load()

    def show(self,user_id) -> str:
        uuid = self.access.lock()
        self.access.wait(uuid)
        if str(user_id) in self.all_historique:
            self.access.unlock(uuid)
            return str(self.all_historique[str(user_id)])
        else:
            self.access.unlock(uuid)
            return "You don't have any command in your historique"
    
    def add(self,user_id,command):
        uuid = self.access.lock()
        self.access.wait(uuid)
        if str(user_id) in self.all_historique:
            self.all_historique[str(user_id)].append(TimeDate() + " " + command)
        else:
            self.all_historique[str(user_id)] = ListChained(TimeDate() + " " +command)
        self.save()
        self.access.unlock(uuid)

    def clear(self,user_id) -> str:
        uuid = self.access.lock()
        self.access.wait(uuid)
        if user_id in self.all_historique:
            del self.all_historique[str(user_id)]
            self.save()
        self.access.unlock(uuid)
        return "Your historique is clear"

    def last(self,user_id):
        uuid = self.access.lock()
        self.access.wait(uuid)
        if user_id in self.all_historique:
            self.access.unlock(uuid)
            return self.all_historique[str(user_id)].firstNode.data
        else:
            self.access.unlock(uuid)
            return "You don't have any command in your historique"


    def save(self):
        '''save the historique in a json file'''
        with open(HISTORY_JSON,"w") as file:
            json.dump(self.all_historique,file,cls=CustomJsonCoder.JsonEncoder)
        

    def load(self):
        '''load the historique from a json file'''
        if not os.path.exists(HISTORY_JSON):
            return
        with open(HISTORY_JSON,"r") as file:
            self.all_historique = json.load(file,cls=CustomJsonCoder.JsonDecoder)

    
def TimeDate():
    return time.strftime("[%d/%m/%Y-%H:%M:%S]", time.localtime())

