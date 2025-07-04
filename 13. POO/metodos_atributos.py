class FabricaTelefonos():
    marca = 'Iphone'
    color = 'Negro'
    memoria_ram = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print('Estás escuchando música')


telefono = FabricaTelefonos()
telefono.marca
telefono.color
telefono.memoria_ram
telefono.almacenamiento

print(telefono.marca)
print(telefono.color)
print(telefono.memoria_ram)
print(telefono.almacenamiento)

print(telefono.llamar('Hola Python'))
telefono.escucharMusica()
