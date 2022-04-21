class Hero:
    #class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private = "private"
        self._protected = "protected"


laba = Hero("laba", 100)

print(laba.__dict__)
print(laba.__private)
print(laba._protected)
print(Hero.__dict__)
print(Hero.__privateJumlah)