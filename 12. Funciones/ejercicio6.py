'''
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
'''

def media(*numeros):
    media = 0
    for numero in numeros:
        media += numero
    return print(f'La media de la secuencia de números es: {media / len(numeros)}')


media(10, 20, 30, 40, 50)
