practica1 = float(input('Introduce la nota de la practica 1: '))
practica2 = float(input('Introduce la nota de la practica 2: '))
practica3 = float(input('Introduce la nota de la practica 3: '))
examen_parcial = float(input('Introduce la nota del examen parcial: '))
examen_final = float(input('Introduce la nota del examen final: '))

promedio_practicas = (practica1 + practica2 + practica3) / 3
promedio = (promedio_practicas + (2 * examen_parcial) + (3 * examen_final)) / 6

print(f'El promedio del curso es: {promedio:.2f}')
