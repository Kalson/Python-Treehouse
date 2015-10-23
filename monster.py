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
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.exp = random.randint(self.min_exp, self.max_exp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)
            # setattr takes 3 arg:
            # self - the object to set the attribute on
            # key - the attribute we want to set
            # value - to give the attribute

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hit_points = 3
    min_hit_points = 3
    max_exp = 2
    min_exp = 2
    sound = "sqeak"


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_exp = 2
    max_exp = 6
    sound = "growl"


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_exp = 6
    max_exp = 10
    sound = "raaaaaaaaaar"

Matt = Goblin()
print(Matt.hit_points)
print(Matt.exp)
print(Matt.color)
print(Matt.battlecry())

Dave = Troll()
print(Dave.hit_points)
print(Dave.exp)
print(Dave.color)
print(Dave.battlecry())

Drake = Dragon()
print(Drake.hit_points)
print(Drake.exp)
print(Drake.color)
print(Drake.battlecry())
