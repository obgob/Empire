__author__ = 'ereid'

from Debug import *
#from Actor import Actor
#from Holding import Holding, Province
from Action import *

test_actor = Actor("Liam Neeson")

debug(test_actor.name, DEBUG_LEVEL_HIGH)

test_holding1 = Holding("Trunamia", test_actor)

test_holding1.upgrade_holding()

test_actor.holdings["Trunamia"] = test_holding1

test_actor.holdings["Trunamia"].upgrade_holding()

test_province = Province("London", test_actor)

test_actor.provinces["London"] = test_province

test_actor.actions['Create Holding'] = create_holding

print test_actor.actions['Create Holding']("Castle", test_actor.provinces["London"], test_actor)

print test_actor.actions.keys()

print test_actor.holdings.keys()

