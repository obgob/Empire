__author__ = 'ereid'

from Actor import Actor
from Holding import Province, Holding
import random

ACTION_SUCCESS = True
ACTION_FAIL = False

class Action:
    def __init__(self, name):
        self.name = name

    def action(self, actor):
        print actor.name + " " + self.name

class CreateHolding(Action):
    def action(self, actor):
        print actor.name + self.name

def create_holding(name, province=Province, actor=Actor):
    chance = Holding.BASE_CHANCE
    random.seed()
    r_num = random.randrange(0, 100)

    if r_num < chance:
        holding = Holding(name, actor)
        province.holdings[name] = holding
        actor.holdings[name] = holding
        return ACTION_SUCCESS
    else:
        return ACTION_FAIL
