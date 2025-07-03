diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
diccionario2 = {'cinco': 5, 'seis': 6}

print(diccionario)
# eliminar un elemento por su clave
diccionario.pop('tres')
print(diccionario)

# recibe la llave como parametro y devuelve el valor
print(diccionario.get('dos'))

# Añade una llave, valor al diccionario
diccionario.setdefault('cuatro', 4)
print(diccionario)

# Actualiza el diccionario original con los datos del diccionario que se le pasa
diccionario.update(diccionario2)
print(diccionario)

# Generar una copia del diccionario
diccionario.copy()
print(diccionario)

# limpiar el diccionario, dejarlo sin datos
diccionario.clear()
print(diccionario)