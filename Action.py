__author__ = 'ereid'

class Action:
    name = "New Action"

    def __init__(self, name):
        self.name = name

    def action(self, actor):
        print actor.name + " " + self.name

class CreateHolding(Action):
    def action(self, actor):
        print actor.name + self.name

