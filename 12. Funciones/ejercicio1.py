'''
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para
agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos
listas nuevas
'''

lista = []
pares = []
impares = []


def agregar():
    for i in range(1, 11):
        numero = int(input('Ingrese un número: '))
        lista.append(numero)


def ordenar():
    for i in range(1, 11):
        numero = lista[i - 1]
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)


agregar()
ordenar()
print(lista)
print(pares)
print(impares)