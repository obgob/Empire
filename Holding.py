__author__ = 'ereid'

from Debug import *
import random
from Actor import Actor

class Holding:

    BASE_CHANCE = 50
    MAX_LEVEL = 10

    def __init__(self, name, owner=Actor):
        self.name = name
        self.level = 0
        self.value = 0
        self.owner = owner

    def change_name(self, new_name):
        self.name = new_name

    def change_owner(self, new_owner=Actor):
        self.owner.holdings.remove(self)
        new_owner.holdings.add(self)
        self.owner = new_owner

    def upgrade_holding(self):
        if self.level < self.MAX_LEVEL:
            random.seed()
            random_num = random.randrange(0, 100)

            if random_num >= self.BASE_CHANCE:
                self.level += 1
                debug(self.owner.name + " successfully upgraded " + self.name + " to level " + self.level.__str__(),
                      DEBUG_LEVEL_MEDIUM)
            else:
                debug(self.owner.name + " failed to upgrade " + self.name, DEBUG_LEVEL_MEDIUM)
        else:
            debug("Cannot upgrade " + self.name + " further", 1)

    def downgrade_holding(self):
        if self.level > 0:
            self.level -= 1

class Province:
    holdings = {}

    def __init__(self, name, owner=Actor):
        self.name = name
        self.owner = owner
