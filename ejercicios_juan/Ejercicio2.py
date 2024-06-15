numero = int(input("Ingrse un numero: "))
suma = 0 
for contador in range(1,numero):

    suma = suma + contador


    if suma > numero:
        print('no es triangular')
        break
    elif suma == numero:
        print('si es triangular')
        break
