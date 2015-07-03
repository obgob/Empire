__author__ = 'ereid'

import Actor, Holding

test_actor = Actor.Actor("Liam Neeson")

print test_actor.name

test_holding1 = Holding.Holding("Trunamia", "", test_actor)

print test_holding1.level

test_holding1.level = 6
test_holding1.level = 1
test_holding1.level = -1

print test_holding1.level

