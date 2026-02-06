n = int(input("¿Cuántos puntos en el espacio desea introducir? "))
lista_puntos = []

for punto in range(n):
    print(f"\nCoordenadas del punto {punto + 1}")
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))
    z = float(input("Ingrese la coordenada z: "))

    match (x, y, z):
        case (x, y, z) if x > 0 and y > 0 and z > 0:
            octante = "I" # Caso: (+, +, +)
        case (x, y, z) if x < 0 and y > 0 and z > 0:
            octante = "II" # Caso: (-, +, +)
        case (x, y, z) if x < 0 and y < 0 and z > 0:
            octante = "III" # Caso: (-, -, +)
        case (x, y, z) if x > 0 and y < 0 and z > 0:
            octante = "IV" # Caso: (+, -, +)
        case (x, y, z) if x > 0 and y > 0 and z < 0:
            octante = "V" # Caso: (+, +, -)
        case (x, y, z) if x < 0 and y > 0 and z < 0:
            octante = "VI" # Caso: (-, +, -)
        case (x, y, z) if x < 0 and y < 0 and z < 0:
            octante = "VII" # Caso: (-, -, -)
        case (x, y, z) if x > 0 and y < 0 and z < 0:
            octante = "VIII" # Caso: (+, -, -)
        case (x, y, z) if x == 0 and y == 0 and z == 0:
            octante = "El punto está en el origen" # Caso: (0, 0, 0)
        case _: # Si la coordenada no existiera:
            octante = "El punto no pertenece a ningún octante" 
    punto = (x, y, z, octante) # guardamos el punto en una tupla
    lista_puntos.append(punto) # agregamos la tupla a la lista de puntos

# Impresion de resultados
print("")
for punto in lista_puntos:
    print(f"El punto ({punto[0]}, {punto[1]}, {punto[2]}) pertenece al octante {punto[3]}")