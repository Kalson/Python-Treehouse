class Monster:
    def __init__(self, hit_points, weapon, color, sound):
        self.hit_points = hit_points
        self.color = color
        self.weapon = weapon
        self.sound = sound

    def battlecry(self):
        return self.sound.upper()


bigfoot = Monster("1", "sword", "green", "meow")
print(bigfoot.color)
print(bigfoot.weapon.upper())
print(bigfoot.battlecry())
