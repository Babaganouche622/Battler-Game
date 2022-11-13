import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, index):
        # print(f"{self.heroes[index].name} dies!")
        for enemy in self.heroes:
            if enemy == index:
                self.heroes.remove(enemy)

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name} Kills: {hero.kills} Deaths: {hero.deaths}")

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f"{hero.name} Health has fully restored!")
