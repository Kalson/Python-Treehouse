class Monster:
    def __init__(self, **sooo):
        self.hit_points = sooo.get("hit_points", 1)
        self.color = sooo.get("color", "green")
        self.weapon = sooo.get("weapon", "sword")
        self.sound = sooo.get("sound", "woof")

    def battlecry(self):
        return self.sound.upper()


bigfoot = Monster(color="red", sound="tweet")
print(bigfoot.color)
print(bigfoot.hit_points)
print(bigfoot.battlecry())
