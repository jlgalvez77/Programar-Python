lista = [1, 2, 3, 4, 5, 'Jose', 'Hamer', 12]
print(lista)

# Agregar un elemento al final de  la lista
lista.append(6)
print(lista)
lista.append('Python')
print(lista)

# Agregar un elemento en una posición especifica de la lista
lista.insert(2, 2.5)
print(lista)

# Cuenta cuantos valores hay en la lista
print(lista.count(5))

# Retorna la posición del parametro que le pasemos, retorna la posición de la primera coincidencia
print(lista.index('Python'))

# Ordenar la lista de manera ascendente, da error si la lista tiene mezclados enteros o flotantes con cadenas
# lista.sort()

# Ordenar la lista de manera descendente
lista.reverse()

# Modificar un valor de la lista
lista[3] = 'Hammer'
print(lista)

# Eliminar el ultimo valor de una lista, este elemento se puede guardar en una variable
eliminado = lista.pop()
print(lista)
print(eliminado)

# Eliminar un valor de la lista, dandole el valor que queremos eliminar
lista.remove('Python')
print(lista)