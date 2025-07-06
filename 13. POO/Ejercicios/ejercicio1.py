'''
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si
ha aprobado o no.
'''

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def mostrarnota(self):
        if (self.nota >= 5):
            print(f"El alumno {self.nombre}, ha sacado {self.nota} y ha aprobado")
        else:
            print(f"El alumno {self.nombre}, ha sacado {self.nota} y ha suspendido")

alumno1 = Alumno('Juan', 4)
alumno1.mostrarnota()