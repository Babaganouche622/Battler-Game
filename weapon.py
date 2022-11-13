import random
class Weapon:
    def __init__(self, name, weapon_type, max_damage, crit_multiplier):
        self.name = name
        self.weapon_type = weapon_type
        self.max_damage = int(max_damage)
        self.damage = self.set_damage()
        self.crit_multiplier = crit_multiplier

    def set_damage(self):
        return random.randint((self.max_damage / 2), self.max_damage)

    def get_damage(self):
        return self.damage