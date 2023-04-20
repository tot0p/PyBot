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
    def __init__(self,historique):
        self.historique = historique
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
        self.load()

    def show(self,user_id) -> str:
        if str(user_id) in self.all_historique:
            return str(self.all_historique[str(user_id)])
        else:
            return "You don't have any command in your historique"
    
    def add(self,user_id,command):
        if str(user_id) in self.all_historique:
            self.all_historique[str(user_id)].append(TimeDate() + " " + command)
        else:
            self.all_historique[str(user_id)] = ListChained(TimeDate() + " " +command)
        self.save()

    def clear(self,user_id) -> str:
        if user_id in self.all_historique:
            del self.all_historique[str(user_id)]
            self.save()
        return "Your historique is clear"

    def last(self,user_id):
        if user_id in self.all_historique:
            return self.all_historique[str(user_id)].firstNode.data
        else:
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

