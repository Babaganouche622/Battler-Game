import random

class Armour:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
        self.defence = self.block()

    def block(self):
        return random.randint(0, self.max_block)
        