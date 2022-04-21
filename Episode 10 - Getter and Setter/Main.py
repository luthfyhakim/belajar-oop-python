class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth : {}".format(self.name, self.__health)

    @property # decorator di python itu analoginya sprt variable ketika di panggil
    def info(self):
        return "name {} : \n\thealth : {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di hapus')
        self.__armor = None


kimbum = Hero('kimbum', 100, 10)

print('=== merubah info ===')
print(kimbum.info) # memanggil method menggunakan decorator sprt memanggil variable biasa
kimbum.name = 'ecobag'
print(kimbum.info)

print('=== getter and setter untuk __armor ===')
print(kimbum.armor) # method getter
kimbum.armor = 50 # method setter
print(kimbum.armor)

print('=== delete armor ===')
del kimbum.armor
print(kimbum.__dict__)