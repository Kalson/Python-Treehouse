class Monster:
    hit_points = 1
    color = "yellow"
    weapon = "sword"
    sound = "roar"

    def battlecry(self):
        return self.sound.upper()


bigfoot = Monster()

print(bigfoot.battlecry())
