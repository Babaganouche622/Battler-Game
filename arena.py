"""
Battle arena set for playing the game.
Here we will have a bunch of functions to bring everything together.
"""


from ability import Ability
from weapon import Weapon
from armour import Armour
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        self.team_one = list()
        self.team_two = list()


    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")
        return Weapon(name, max_damage)

    def create_armour(self):
        name = input("What is the armour name? ")
        max_damage = input("What is the max damage of the armour? ")
        return Armour(name, max_damage)

    def create_hero(self):
        hero_name = input("What's your hero's name? ")
        hero = Hero(hero_name)
        add_item = None
        building_hero = True
        while building_hero:
            choice = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            match choice:
                case "1":
                    hero.add_ability(self.create_ability())
                case "2":
                    hero.add_weapon(self.create_weapon())
                case "3":
                    hero.add_armour(self.create_armour())
                case "4":
                    return hero
                case _:
                    print(f"{choice} not recognized. Make a new selection.\n")

    def build_team(self):
        team_name = input("What is your team name? ")
        team = Team(team_name)
        building_team = True
        while building_team:
            choice = input("Would you like to add a party member?\n[1] Yes\n[2] No\n\n Your choice: ")
            match choice:
                case "1":
                    team.add_hero(self.create_hero())
                case "2":
                    building_team = False 
                    return team
                case _:
                    print(f"{choice} not recognised. Make a new selection.\n")
                    
    def build_arena(self):
        building_arena = True
        while building_arena:
            choice = input("Which team are we building?\n[1] Team one\n[2] Team two\n[3] Finished\n\n Your choice: ")
            match choice:
                case "1":
                    self.team_one = self.build_team()
                case "2":
                    self.team_two = self.build_team()
                case "3":
                    building_arena = False
                case _:
                    print(f"{choice} not recognised. Make a new selection.\n")

    def team_battle(self):
        self.team_one.attack(self.team_two)

    

