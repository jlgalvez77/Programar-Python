'''
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de
Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos
transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
'''

class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

    @property
    def llantas(self):
        return self._llantas

    @llantas.setter
    def llantas(self, llantas):
        self._llantas = llantas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio


class Moto(Fabrica):
    def llantas(self):
        return self._llantas

    def color(self):
        return self._color

    def precio(self):
        return self._precio


class Coche(Fabrica):
    def llantas(self):
        return self._llantas

    def color(self):
        return self._color

    def precio(self):
        return self._precio


if __name__ == '__main__':
    moto = Moto(2, "Rojo", 3000)
    print(f"La moto tiene {moto.llantas()} llantas, es de color: {moto.color()} y cuesta {moto.precio()} euros.")

    coche = Coche(4, "Negro", 32000)
    print(f"El coche tiene {coche.llantas()} llantas, es de color: {coche.color()} y cuesta {coche.precio()} euros.")
