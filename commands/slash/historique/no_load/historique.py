#-*- coding: utf-8 -*-

from dataType.Stack import Stack


class Historique(Stack):
    def __init__(self, first_data):
        super().__init__(first_data)

    def __str__(self) -> str:
        return super().__str__()