while True:
    try:
        num1 = int(input('Ingresa un numero: '))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
    except ValueError:
        print('Valor erroneo.')
    except KeyboardInterrupt:
        print('\nHas cancelado la ejecución')