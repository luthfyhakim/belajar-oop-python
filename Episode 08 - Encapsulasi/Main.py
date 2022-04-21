class Hero:

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru):
        self.__attPower = nilaiBaru


# awal dari game
laba = Hero("laba", 100, 20)

# game berjalan
print(laba.getName())
print(laba.getHealth())
laba.diserang(5)
print(laba.getHealth())