import random
from random import randint
from ability import Ability
from armour import Armour

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armours = list()
        self.weapons = list()


    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            opponent.take_damage(hero.attack())
            hero.take_damage(opponent.attack())
            print(hero.current_health)
            print(opponent.current_health)
        if hero.is_alive() == False:
            print(f"{self.name} has perished.")
        if opponent.is_alive() == False:
            print(f"{opponent.name} has perished.")
        
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armour(self, armour):
        self.armours.append(armour)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_defence = 0
        for armour in self.armours:
            total_defence += armour.block()
        return total_defence

    def take_damage(self, damage):
        true_damage = damage - self.defend()
        if true_damage > 0:
            self.current_health -= true_damage
            print(f"{self.name} Took {true_damage} damage!")
        else:
            print(f'{self.name} Took no damage!')

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False



if __name__ == "__main__":
    hero = Hero("Goku", 500)
    enemy = Hero("Vegeta", 500)
    gi = Armour("Gi", 50)
    fire_ball = Ability("Fire Ball", 100)
    hero.add_armour(gi)
    enemy.add_armour(gi)
    hero.add_ability(fire_ball)
    enemy.add_ability(fire_ball)
    hero.fight(enemy)
    # while hero.is_alive() == True or enemy.is_alive() == True:
    #     hero.attack(enemy)
    #     enemy.attack(hero)
    # print(hero.current_health)
    # print(enemy.current_health)