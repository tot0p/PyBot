#-*- coding: utf-8 -*-

from dataType.ListChained import ListChained

import time

class Historique:
    def __init__(self):
        self.all_historique = {} 

    def show(self,user_id):
        if user_id in self.all_historique:
            return str(self.all_historique[user_id])
        else:
            return "You don't have any command in your historique"
    

    def add(self,user_id,command):
        if user_id in self.all_historique:
            self.all_historique[user_id].append(TimeDate() + " " + command)
        else:
            self.all_historique[user_id] = ListChained(TimeDate() + " " +command)


    def clear(self,user_id):
        del self.all_historique[user_id]

    def last(self,user_id):
        if user_id in self.all_historique:
            return self.all_historique[user_id].firstNode.data
        else:
            return "You don't have any command in your historique"

    
def TimeDate():
    return time.strftime("[%d/%m/%Y-%H:%M:%S]", time.localtime())