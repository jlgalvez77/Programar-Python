'''
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''

i = 1
numero = int(input('Introduce el numero de la tabla de multiplicar que quieres ver: '))
while i <= 10:
    print(f'{i} x {numero} = {i * numero}')
    i += 1
