'''
Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad).
Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima
llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre
y universidad de dicho estudiante con un objeto llamado persona.
'''


class Universidad():
    def __init__(self, nombre_universidad):
        self.nombre_universidad = nombre_universidad


class Carrera():
    def __init__(self, especialidad):
        self.especialidad = especialidad


class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años, mi especialidad es {self.especialidad} "
              f"y mi Universidad es {self.nombre_universidad}")


persona = Estudiante("Universidad de Oviedo")
persona.especialidad = "Ingenieria Informática"
persona.datos("José Gálvez", 48)

