while True:
    try:
        edad = int(input('Ingrese la edad: '))
        print(f'Edad: {edad}')
        break
    except:
        print('El edad no es valido')
    finally:
        print('Esta linea se imprime siempre.')