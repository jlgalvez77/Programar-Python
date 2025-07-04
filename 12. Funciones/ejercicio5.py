import math


'''
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura;
y la otra el area de un circulo con argumento de radio
'''

def area(base, altura):
    area = base * altura
    return area


def circulo(radio):
    area = math.pi * radio ** 2
    return area


print(area(10, 20))
print(circulo(10))