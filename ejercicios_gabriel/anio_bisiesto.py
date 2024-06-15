def is_anio_bisiesto(anio):
    if anio % 4 == 0 and ((not anio % 100 == 0) or anio % 400 == 0):
        return True
    return False

while True:
    anio = int(input("Introduce un año para saber si es bisiesto: "))
    if is_anio_bisiesto(anio):
        print("Es año bisiesto.")
    else:
        print("No es año bisiesto.")
        
    continuar = input("¿Continuar? (s/n): ")
    if continuar != "s":
        break
