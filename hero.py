import random

class Hero:
    def __init__(self, name, starting_health=500):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armours = list()
        self.weapons = list()
        self.deaths = 0
        self.kills = 0


    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
            print(self.current_health)
            print(opponent.current_health)
        if self.is_alive() == False:
            self.add_death()
            opponent.add_kill()
            print(f"{self.name} has perished.")
        if opponent.is_alive() == False:
            self.add_kill()
            opponent.add_death()
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

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1
