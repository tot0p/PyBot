#-*- coding: utf-8 -*-

from dataType.ListChained import ListChained
import time

from constant import HISTORY_JSON

import json
import os

from tools import CustomJsonCoder 


class Historique:
    def __init__(self):
        self.all_historique = {} 
        self.load()

    def show(self,user_id):
        if str(user_id) in self.all_historique:
            return str(self.all_historique[str(user_id)])
        else:
            return "You don't have any command in your historique"
    
    def add(self,user_id,command):
        if str(user_id) in self.all_historique:
            self.all_historique[str(user_id)].append(TimeDate() + " " + command)
        else:
            self.all_historique[str(user_id)] = ListChained(TimeDate() + " " +command)

    def clear(self,user_id):
        if user_id in self.all_historique:
            del self.all_historique[str(user_id)]

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

