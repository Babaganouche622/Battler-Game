import random

class Armour:
    """
    All armour will have a Name, Max Block, Calculated Defence total
    New Armour class children may come as armour library grows.
    """
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
        self.defence = self.set_defence()

    def set_defence(self):
        """Armour will always set each piece with a defence ratio between 80% - 100% of max block"""
        ratio = self.max_block * 0.8
        return random.randint(round(ratio), self.max_block)

    def get_defence(self):
        """Generic getter for the defence stat"""
        return self.defence

    def get_name(self):
        """Generic getter for the item name"""
        return self.name
        