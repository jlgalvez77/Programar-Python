numero = int(input('Ingresa un numero entero: '))

if numero > 0:
    numero_absoluto = numero
    print(f'El número absoluto de {numero} es {numero_absoluto}')
elif numero < 0:
    numero_absoluto = numero * -1
    print(f'El número absoluto de {numero} es {numero_absoluto}')
elif numero == 0:
    numero_absoluto = 0
    print(f'El número absoluto de {numero} es {numero_absoluto}')
else:
    print('Debes introducir un número entero')