__author__ = 'ereid'

from Debug import *

class Actor:

    name = ""
    provinces = {}
    holdings = {}
    vassals = {}
    superior = None
    actions = {}
    num_actions = 1

    def __init__(self, name):
        self.name = name
        self.level = "Count"
