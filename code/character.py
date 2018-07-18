# Character class


class Character:
    """Used to make the player character and enemy NPCs"""

    def __init__(self, name, current_hp, max_hp, inventory):
        self.name = name
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.inventory = inventory = {}

    def checkhealth(self):
        if self.current_hp == self.max_hp:
            return 'You feel great'
        elif self.max_hp / 2 < self.current_hp < self.max_hp:
            return 'You have a few scrapes and bruises'
        elif self.max_hp / 6 < self.current_hp <= self.max_hp / 2:
            return 'You are bloodied'
        elif self.current_hp <= self.max_hp / 6:
            return 'You are very bloodied and broken. Death is knocking.'