palabra1 = input('Ingresa una palabra 1: ')
palabra2 = input('Ingresa una palabra 2: ')

if palabra1[-3:] == palabra2[-3:]:
    print('Las palabras riman')
elif palabra1[-2:] == palabra2[-2:]:
    print('Las palabras riman un poco')
else:
    print('Las palabras no riman')
