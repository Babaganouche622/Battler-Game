import random
import pygame
from game_object import GameObject
from weapon import Weapon
from armour import Armour
from button import Button

class Hero(GameObject):
    """
    This is our large hero class. 
    Currrently being used to build too much.
    Every creature needs:
    Name, Image, Starting HP, Weapon, Equipment list, Unit Damage, Unit Armour rating, Crit Chance, Accuracy, 
    Needs to be broken into 7 sub classes:
    Paladin, White mage, Summoner, Ninja, Dragoon, basic enemy, Boss.
    Things to move:
    Experience, Buttons, Special(), Display Stats().
    """
    def __init__(self, image, name, starting_health=500, damage=0):
        super(Hero, self).__init__(50, 50, image)
        self.name = name
        self.max_health = starting_health
        self.current_health = starting_health
        self.weapon = Weapon
        self.equipment = list()
        self.damage = damage
        self.armour = 0
        self.crit_chance = 0
        self.attack_button = Button
        self.special_button = Button
        self.experience = 0

    def add_attack_button(self, button):
        self.attack_button = button

    def add_special_button(self, button):
        self.special_button = button

    def attack(self, opponent):
        """
        Roll crit chance, apply damage to opponent
        Need to add Miss chance.
        """
        roll = random.randint(0, 100)
        damage = self.damage
        if roll < self.crit_chance:
            damage = self.damage * self.weapon.crit_multiplier
        opponent.take_damage(damage)
        print(f"{self.name} hits {opponent.name} for {damage}!")

    def special(self):
        """This is the class specific special ability"""
        pass

    def take_damage(self, damage):
        """take the opponent's damage roll and subtract this Hero's armour rating, then apply the damage left over"""
        true_damage = damage - self.armour
        if true_damage > 0:
            self.current_health -= true_damage
            print(f"{self.name} Took {true_damage} damage!")

    def add_equipment(self, item):
        """
        Add a weapon, only 1 at a time right now.
        Add infinit armour right now
        Check for specific Class instance
        """
        if isinstance(item, Weapon):
            self.weapon = item
            self.damage = item.get_damage()
        if isinstance(item, Armour):
            self.equipment.append(item)
            self.armour += item.get_defence()

    def is_alive(self):
        """Check if the Hero is alive or dead"""
        if self.current_health > 0:
            return True
        else:
            return False

    def add_experience(self, experience):
        self.experience += experience

    def display_equipment(self):
        """This method is only here to loop the items in the equipment list for the display_stats() method."""
        string = ""
        for item in self.equipment:
            string += item.name
        return string

    def display_stats(self):
        """
        Display all the stats of the given hero in a clean console log for now
        """
        print(
f"""
|-------------------------------------|
| Name: {self.name} 
| Weapon: {self.weapon.name}
| Damage: {self.damage}
| Equipment: {self.display_equipment()}
| Armour: {self.armour}
| Current Health: {self.current_health}
| Experience: {self.experience}
|-------------------------------------|
        
""")
