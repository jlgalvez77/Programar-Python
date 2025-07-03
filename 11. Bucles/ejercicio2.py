'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad).
'''

i = 1
edad = int(input('Introduce tu edad: '))
while i <= edad:
    print(f'Has cumplido {i} años')
    i += 1
