__author__ = 'ereid'

import random, Actor

class Holding:

    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self._level = 1
        self.value = 0

    def change_name(self, new_name):
        self.name = new_name

    @property
    def level(self):
        print "get test"
        return self._level

    @level.setter
    def level(self, value):
        print "set test"
        if value == -1:
            if self._level == 0:
                print "Error: Holding level cannot go below 0"
            self._level -= 1
        elif value == 1:
            self._level += 1
        else:
            print "Error: Holding level can only change by +/-1"

    def change_owner(self, new_owner=Actor.Actor("Unknown")):
        self.owner.holdings.remove(self)
        new_owner.holdings.add(self)
        self.owner = new_owner

holding = Holding("test", "England", Actor.Actor("Tom Riddle"))

print holding.level