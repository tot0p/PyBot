#-*- coding: utf-8 -*-
from dataType.AwTree import AwTree
from dataType.HashTable import HashTable

import json

def HashTableLoadJson(path):
    with open(path, "r") as file:
        data =  json.load(file)
    
    temps = []

    for key,value in data:
        temp = AwTree()
        temp.loadJson(value)
        temps.append((key,temp))

    return HashTable(temps)    