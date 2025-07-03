conjunto = {1, 2, 3, 3, 4, 4, 5}
lista = [1, 1, 2, 3, 4, 4]
print(lista)
# En un conjunto no ha datos repetidos
print(conjunto)

# Añade un nuevo valor al conjunto
conjunto.add(20)
print(conjunto)

# Elimina un valor del conjunto
conjunto.discard(20)
conjunto.remove(1)

# Elimina al azar un valor del conjunto
conjunto.pop()
print(conjunto)

# Añades elementos iterables al conjunto
conjunto.update([1, 2, 3])

# Elimina los datos del conjunto
conjunto.clear()
