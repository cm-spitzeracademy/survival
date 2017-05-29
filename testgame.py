#!/usr/bin/env python

from Survival.Items import Weapons
from Survival.People import Villager

sword = Weapons('longsword', 30)

print("%s\n" % sword.stats())


villager1 = Villager('Robert', 40, 20, 30)
villager2 = Villager('Nathan', 40, 20, 30)

print("Here are our villagers:")
print("%s\n" % villager1.stats())
print("%s\n" % villager2.stats())

villager1.remove_life(5)
print("Our villager is hurt:")
print("%s\n" % villager1.stats())

villager1.add_life(5)
print("Our villager takes a healing potion:")
print("%s\n" % villager1.stats())

villager2.add_strength(5)
villager2.add_defense(5)
print("Villager2 finds a sword:")
print("%s\n" % villager2.stats())

villager2.add_defense(5)
villager2.add_life(5)
print("Villager2 finds a shield:")
print("%s\n" % villager2.stats())
