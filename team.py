from hero import Hero
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
        if not found_hero:
            return 0        
        

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Death:{kd}")

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f"{hero.name} Health has fully restored!")

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)
        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            fighter1 = random.choice(living_heroes)
            fighter2 = random.choice(living_opponents)
            fighter1.attack(fighter2)
            if fighter1.current_health < 0:
                living_heroes.remove(fighter1)
            if fighter2.current_health < 0:
                living_opponents.remove(fighter2)


        self.status()
        other_team.status()

        if len(living_heroes) > 0:
            print(f"{self.name} Have won the fight!")
        if len(living_opponents) > 0:
            print(f"{other_team.name} Have won the fight!")

