n = int(input("¿Cuántos números complejos desea introducir? "))

lista_tuplas_complejos = [] #Creamos una lista para almacenar todas las tuplas

for numero in range(n):
    #Limpiamos la entrada para evitar errores con espacios
    entrada_usuario = input(f"Ingrese el número complejo {numero + 1} (ej. 1+1j): ")
    z = complex(entrada_usuario.replace(" ", ""))

    #Realizamos las operaciones de opuesto y conjugado
    opuesto = -z
    conjugado = complex(z.real, -z.imag)

    #Guardamos los numeros en una tupla y luego esa tupla la agregamos a la lista
    tupla = (z, opuesto, conjugado)
    lista_tuplas_complejos.append(tupla)

#Iteramos sobre la lista de tuplas para imprimir los resultados
print("\nLos resultados son: ")
for z, opuesto, conjugado in lista_tuplas_complejos:
    print(f"Original: {z}, Opuesto: {opuesto}, Conjugado: {conjugado}")