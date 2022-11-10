from hero import Hero


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




