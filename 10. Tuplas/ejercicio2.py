'''
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado,
es la letra que debe imprimir el programa
'''

alfabeto = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z')

letra = int(input('Introduce el número de letra: '))
print(f'La letra número {letra} es la {alfabeto[letra-1]}')
