'''
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros
entre ambas cifras
'''

i = 1
while i <= 10:
    print(i)
    i += 1

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))

if numero1 > numero2:
    print('El primer número no puede ser mayor que el segundo.')
else:
    for numero in range(numero1, numero2 + 1):
        print(numero)