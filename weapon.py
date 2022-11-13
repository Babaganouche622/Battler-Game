import random
class Weapon:
    """
    Weapons are built premade inside a library that can be used to populate
    loot for the heroes.
    All wepons have: Name, Type, Max Damage, Crit Multiplier, Miss ratio.
    """
    def __init__(self, name, weapon_type, max_damage, crit_multiplier):
        self.name = name
        self.weapon_type = weapon_type
        self.max_damage = int(max_damage)
        self.damage = self.set_damage()
        self.crit_multiplier = crit_multiplier

    def set_damage(self):
        """Damage is always set as a variable of half the top half of total damage (50% - 100%)"""
        return random.randint((self.max_damage / 2), self.max_damage)

    def get_damage(self):
        """Generic getter to return the calculated damage of this item"""
        return self.damage

    def get_name(self):
        """Generic getter to return this weapon's given calculated damage"""
        return self.name

    def get_weapon_type(self):
        """Generic getter to return this weapon's given weapon type"""
        return self.weapon_type

    def get_crit_multiplier(self):
        """Generic getter to return this weapon's given crit multiplier"""
        return self.crit_multiplier
        