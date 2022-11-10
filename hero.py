import random
from random import randint

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        winner = self.current_health / (self.current_health + opponent.current_health)
        if winner == 1:
            print(self.name)
        else:
            print(opponent.name)
        





if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)