'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo
los números que sean impares
'''

numero1 = int(input("Ingrese un número: "))
numero2 = int(input('Introduce otro número: '))

for numero in range(numero1, numero2 + 1):
    if numero % 2 == 0:
        continue
    else:
        print(numero)