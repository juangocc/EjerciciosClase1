def is_numero_armstrong(numero):
    suma = 0
    for digito in numero:
        suma += pow(int(digito), len(numero))

    if suma == int(numero):
        return True
    
    return False

while True:
    numero = input("Introduce un año para saber si es numero Armstrong: ")
    if is_numero_armstrong(numero):
        print("Es numero Armstrong.")
    else:
        print("No es un numero Armstrong.")
        
    continuar = input("¿Continuar? (s/n): ")
    if continuar != "s":
        break
