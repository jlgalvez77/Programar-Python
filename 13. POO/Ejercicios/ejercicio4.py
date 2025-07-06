'''
Escribir una clase que se llame Areas(). A partir de un constructor se deben pasar los valores de Base y Altura. Luego,
se debe calcular area de un cuadrado, triangulo y pentagono
'''


class Areas():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def cuadrado(self):
        return self.base * self.altura

    def triangulo(self):
        area = self.base * self.altura / 2
        return f"El area del triangulo es: {area}"

    def pentagono(self):
        area = self.base * self.altura * 0.5
        return f"El area del pentagono es: {area}"


areas = Areas(4, 2)
print(f"El area del cuadrado es: {areas.cuadrado()}")
print(areas.triangulo())
print(areas.pentagono())
