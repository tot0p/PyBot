#-*- coding: utf-8 -*-
from dataType.AwTree import AwTree
from dataType.HashTable import HashTable

from config import AWTREE_HASH_TABLE_JSON

import json

def _HashTableLoadJson(path) -> HashTable:
    with open(path, "r") as file:
        data =  json.load(file)
    
    temps = []

    

    for key in data.keys():
        value = data[key]
        temp = AwTree()
        temp.loadJson(value)
        temps.append((key,temp))

    return HashTable(temps)    


def LoadAwTreeHashTable():
    return _HashTableLoadJson(AWTREE_HASH_TABLE_JSON)