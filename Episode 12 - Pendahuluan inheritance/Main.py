class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health


class Hero_intelligent(Hero):
    pass


class Hero_strength(Hero):
    pass


meeev = Hero('meeev', 100)
chiq = Hero_intelligent('chiq', 50)
inhe = Hero_strength('inhe', 70)

print(meeev.name)
print(chiq.name)
print(inhe.name)