'''
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe
mostrar en la tupla
'''

meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiempre', 'Octubre',
         'Noviembre', 'Diciembre')

mes = int(input('Introduce el número de mes: '))
if mes < 0 or mes > 12:
    print('Mes inválido')
else:
    print(f'El mes {mes} es {meses[mes-1]}')
