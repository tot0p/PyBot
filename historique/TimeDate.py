#-*- coding: utf-8 -*-

import time

def TimeDate():
    return time.strftime("[%d/%m/%Y-%H:%M:%S]", time.localtime())