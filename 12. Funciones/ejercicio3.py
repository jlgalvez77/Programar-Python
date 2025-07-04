'''
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el
segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
'''

def numeros(numero1, numero2):
    if numero1 > numero2:
        return 1
    elif numero1 < numero2:
        return -1
    else:
        return 0

print(numeros(3, 3))