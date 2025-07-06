class FabricaTelefonoe():
    def __init__(self, marca, color, *args, **kwargs):
        self.marca = marca
        self.color = color
        self.args = args
        self.kwargs = kwargs


telefono = FabricaTelefonoe("Iphone", "Negro", "500g", largo = 270)
print(telefono.marca)
print(telefono.color)
print(telefono.args)
print(telefono.kwargs)
# Este atributo solo es asignado a este objeto
telefono.memoria = 512