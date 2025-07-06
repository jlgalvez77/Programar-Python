'''
Escribir una clase en python que calcule pow(x, n)
x = es la base
n = es el exponente
'''

class Exponente:
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcular(self):
        return self.base**self.exponente

exponente = Exponente(4, 2)
print(exponente.calcular())