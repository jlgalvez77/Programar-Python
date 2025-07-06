class FabricaTelefonos():
    # Metodo constructor
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print(f"El objeto {self.marca} ha sido creado")

    def __str__(self):
        return f"El objeto es {self.marca}"

    # Metodo destructor
    def __del__(self):
        print("El objeto ha sido destruido")


telefono = FabricaTelefonos("Nokia", "Negro")
print(telefono.marca)
print(telefono.color)
print(telefono)