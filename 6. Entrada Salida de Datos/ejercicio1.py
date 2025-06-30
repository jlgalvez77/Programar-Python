from math import sqrt

valor_a = float(input('Introduce el valor de a: '))
valor_b = float(input('Introduce el valor de b: '))
valor_c = float(input('Introduce el valor de c: '))
x1 = 0
x2 = 0

if ((valor_b ** 2) - (4 * valor_a * valor_c)) < 0:
    print('No es posible llevar a cabo la operación porque no se puede sacar la raiz de un número negativo.')
else:
    x1 = (-valor_b + sqrt(((valor_b ** 2) - (4 * valor_a * valor_c))) / (2 * valor_a))
    x2 = (-valor_b - sqrt(((valor_b ** 2) - (4 * valor_a * valor_c))) / (2 * valor_a))
    print(f'La solución es: \nx1 = {x1}  \nx2 = {x2}')
