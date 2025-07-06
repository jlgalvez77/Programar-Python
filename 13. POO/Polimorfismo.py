class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)


class Perro(Animales):
    def hablar(self):
        print("Yo hago Guau")


class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")


animal = Animales("Miau")
animal.hablar()

perro = Perro("Guau")
perro.hablar()

pez = Pez("Nada")
pez.hablar()

