palabras = [] #lista vacia para guardar palabras

while True:
    palabra = input("Ingrese una palabra (presione Enter para terminar): ")
    if palabra == "": #si la palabra esta vacia, salimos del bucle
        break
    palabras.append(palabra) #agregamos la palabra a la lista
    
if len(palabras) >= 2:
    tupla = tuple(palabras) #guardamos las palabras de la lista en una tupla
    
    # La primer palabra (indice 0) es capturada con palabra1
    # *_ descarta todas las palabras que estan en medio
    # La ultima palabra (indice -1) es capturada con palabra2
    palabra1, *_, palabra2 = tupla

    print(f"La primera palabra es: {palabra1}")
    print(f"La última palabra es: {palabra2}")

elif len(palabras) == 1:
    print(f"La única palabra introducida es: {palabras[0]}")
else:
    print("No se introdujeron palabras.")