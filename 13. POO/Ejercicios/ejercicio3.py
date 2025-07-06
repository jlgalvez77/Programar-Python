'''
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular
después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
'''


class Calculadora:
    def __init__(self):
        self.a = int(input("Ingresa el primer número: "))
        self.b = int(input("Ingresa el segundo número: "))

    def suma(self):
        self.suma = self.a + self.b
        print(f"La suma da como resultado: {self.suma}")

    def resta(self):
        self.resta = self.a - self.b
        print(f"La resta da como resultado: {self.resta}")

    def multiplicacion(self):
        self.multiplicacion = self.a * self.b
        print(f"La multiplicación da como resultado: {self.multiplicacion}")

    def division(self):
        self.division = self.a / self.b
        print(f"La division da como resultado: {self.division}")


calculadora = Calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()
