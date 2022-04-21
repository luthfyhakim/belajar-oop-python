class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object saja
    def getJumlah(self): # parameter (self) terserah mau tulis apa aja
        return Hero.__jumlah

    # method ini hanya berlaku untuk class saja
    def getJumlah1():
        return Hero.__jumlah

    # method static (decorator) nempel ke object dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls): # parameter terserah mau tulis apa aja
        return cls.__jumlah


hakim = Hero('hakim')
print(Hero.getJumlah1())
ecobag = Hero('ecobag')
print(ecobag.getJumlah2())
kimbum = Hero('kimbum')
print(kimbum.getJumlah3())