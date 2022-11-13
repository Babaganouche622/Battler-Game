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

    def add_experience(self, experience):
        each_experience = round(int(experience) / len(self.heroes))
        for hero in self.heroes:
            hero.add_experience(int(each_experience))

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f"{hero.name} Health has fully restored!")
