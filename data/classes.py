class Character:
    def __init__(self, empty=True, variation=0, health=0, attack=0, armor=0):
        self.empty = empty
        self.variation = variation
        self.health = health
        self.attack = attack
        self.armor = armor


class Item:
    def __init__(self, empty=True, health_gain=0, attack_gain=0, armor_gain=0):
        self.empty = empty
        self.health_gain = health_gain
        self.attack_gain = attack_gain
        self.armor_gain = armor_gain


class Tile:
    def __init__(self, structure, character, item):
        self.structure = structure
        self.character = character
        self.item = item
23