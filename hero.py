import random
import pygame
from game_object import GameObject
from weapon import Weapon
from armour import Armour

class Hero(GameObject):
    def __init__(self, image, name, starting_health=500):
        super(Hero, self).__init__(50, 50, image)
        self.name = name
        self.max_health = starting_health
        self.current_health = starting_health
        self.weapon = Weapon
        self.equipment = list()
        self.deaths = 0
        self.kills = 0
        self.damage = 0
        self.armour = 0
        self.crit_chance = 0


    def attack(self,opponent):
        opponent.take_damage(self.damage)

    def special(self):
        """This is the class specific special ability"""
        pass

    def take_damage(self, damage):
        true_damage = damage - self.armour
        if true_damage > 0:
            self.current_health -= true_damage
            print(f"{self.name} Took {true_damage} damage!")

    def add_equipment(self, item):
        if isinstance(item, Weapon):
            self.weapon = item
            self.damage += item.damage
        if isinstance(item, Armour):
            self.equipment.append(item)
            self.armour += item.defence

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1


