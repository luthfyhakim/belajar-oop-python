class Mangga:

    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # method ini biasanya digunakan ketika proses debugging
    def __repr__(self):
        return "Debug -- Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)

    # method ini biasanya digunakan pada production kegunaannya sama dgn method __repr__
    def __str__(self):
        return "Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)

    # utk menambahkan 2 buah objek
    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"


belanja1 = Mangga("arumanis", 10)
belanja2 = Mangga("mana lagi", 30)

print(belanja1) # --> method str
print(belanja2)
print(belanja1 + belanja2) # --> method add
print(belanja1.__dict__)