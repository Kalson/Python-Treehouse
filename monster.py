import random
COLORS = ["red", "green", "blue", "white"]


class Monster:
    max_hit_points = 1
    min_hit_points = 1
    max_exp = 1
    min_exp = 1
    weapon = "sword"
    sound = "yeti-roar"

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.max_hit_points, self.min_hit_points)
        self.exp = random.randint(self.max_exp, self.min_exp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)
            # setattr takes 3 arg:
            # self - the object to set the attribute on
            # key - the attribute we want to set
            # value - to give the attribute

    def battlecry(self):
        return self.sound.upper()


bigfoot = Monster()
print(bigfoot.color)
print(bigfoot.hit_points)
print(bigfoot.battlecry())

print("=========")

lochness = Monster(color="blue-green", hit_points=500, sound="yawn", adjective="manxsome")
print(lochness.color)
print(lochness.hit_points)
print(lochness.adjective)
print(lochness.battlecry())
