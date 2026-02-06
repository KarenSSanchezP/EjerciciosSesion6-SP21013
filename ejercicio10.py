#Llenado de las listas lis1 y lis2
n = int(input("Ingrese la cantidad de elementos de la lista 1: "))
lis1 = [int(input(f"Elemento {i+1} de lista 1: ")) for i in range(n)]

m = int(input("Ingrese la cantidad de elementos de la lista 2: "))
lis2 = [int(input(f"Elemento {j+1} de lista 2: ")) for j in range(m)]

#Convertimos las listas a conjuntos
set1 = set(lis1)
set2 = set(lis2)

#Operacion de conjuntos
set_intersection = set1 & set2
set_sym_difference = set1.symmetric_difference(set2)
set_difference1 = set1 - set2
set_difference2 = set2 - set1

#Lista de conteos
lis_conteos = [len(set_intersection), len(set_sym_difference), len(set_difference1), len(set_difference2)]

#Impresion de resultados
print("-" * 26)
print(f"Resultado: {lis_conteos}\n")
print(f"{lis_conteos[0]} elementos presentes en ambas matrices: {set_intersection}")
print(f"{lis_conteos[1]} elementos presentes en una sola matriz: {set_sym_difference}")
print(f"{lis_conteos[2]} elementos restantes en la matriz 1: {set_difference1}")
print(f"{lis_conteos[3]} elementos restantes en la matriz 2: {set_difference2}")