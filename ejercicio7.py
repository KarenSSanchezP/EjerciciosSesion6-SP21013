dicc1 = dict()
n = int(input("Ingrese el número de elementos del primer diccionario: "))

for i in range(n):
    key = input(f"Ingrese la clave {i+1}: ")
    value = int(input(f"Ingrese el valor para '{key}': "))
    if key not in dicc1: # Si la clave aun no esta en dicc1,
        dicc1[key] = []    # se crea una lista asociada a esa clave
    dicc1[key].append(value) # Agrega el valor ingresado a la lista de la clave correspondiente

dicc2 = dict()
m = int(input("Ingrese el número de elementos del segundo diccionario: "))

for j in range(m):
    key = input(f"Ingrese la clave {j+1}: ")
    value = int(input(f"Ingrese el valor para '{key}': "))
    if key not in dicc2: # Si la clave aun no esta en dicc2,
        dicc2[key] = []    # se crea una lista asociada a esa clave
    dicc2[key].append(value) # Agrega el valor ingresado a la lista de la clave correspondiente

diccResultado = dict()

# Recopilamos todas las claves de ambos diccionarios en una lista
all_keys = list(dicc1.keys()) + list(dicc2.keys())

# Obtenemos solo las claves únicas de la lista
all_unique_keys = []
for key in all_keys:
    if key not in all_unique_keys: # Nos aseguramos de que solo se agregue si aun no esta ahi
        all_unique_keys.append(key)

for key in all_unique_keys:
    values_for_key = [] # Lista para acumular los valores por clave
    if key in dicc1:
        values_for_key.extend(dicc1[key]) # Usamos extend porque dicc1[key] ya es una lista
    if key in dicc2:
        values_for_key.extend(dicc2[key]) # Usamos extend porque dicc2[key] ya es una lista
    diccResultado[key] = values_for_key # Guardamos los valores de esa clave en el diccionario resultado

print(diccResultado)