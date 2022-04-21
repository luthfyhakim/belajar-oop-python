# method resolution order 

class A:
    def show(self):
        print("ini adalah show A")


class B:
    def show(self):
        print("ini adalah show B")


class C (B, A): # sesuai urutan inheritance 
    pass


objek = C()
objek.show()
# help(objek)