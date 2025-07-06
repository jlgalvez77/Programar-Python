class Animales():
    def emite_sonido(self):
        print('Emite sonido')

    def descripcion(self):
        print(f"Yo soy un {self.animal}")

class Perro(Animales):
    pass


class Abeja(Animales):
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.emite_sonido()

perro = Perro()
perro.emite_sonido()

abeja = Abeja("Abeja")
abeja.descripcion()