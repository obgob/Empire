__author__ = 'ereid'


class Actor:

    name = ""
    holdings = []
    vassals = []
    superior = None
    actions = []
    num_actions = 1

    def __init__(self, name):
        self.name = name
        self.level = "Count"
