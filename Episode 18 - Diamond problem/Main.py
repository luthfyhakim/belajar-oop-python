class A:
    def show(self):
        print("ini adalah show A")


class B (A):
    def show(self):
        print("ini adalah show B")


class C (A):
    def show(self):
        print("ini adalah show C")


class D (B, C):
    pass


objek = D() # urutannya dari class D -> B -> C -> A
objek.show()