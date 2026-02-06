import requests

def limpiar_ki(ki_str):
    #Nos aseguramos de que el ki sea un string en minusculas y sin espacios
    ki_str = str(ki_str).lower().strip() 
    #Manejamos los valores no numericos
    if ki_str in ["unknown", "???", "0"]:
        return 0
    #Definimos las magnitudes
    magnitudes = {
        "googolplex": 10 ** 100, #simbolico, sino me explota la laptop
        "septillion": 10 ** 24, 
        "quintillion": 10 ** 18,
        "quadrillion": 10 ** 15,
        "trillion": 10 ** 12,
        "billion": 10 ** 9,
        "million": 10 ** 6,
    }

    #quitamos los puntos y comas de miles para normalizar los numeros
    ki_limpio = ki_str.replace(".", "").replace(",", "")

    #Intercambiamos los valores en palabras (ej. billion) por su valor numerico (ej. 10 ** 9)
    for palabra, valor in magnitudes.items():
        if palabra in ki_limpio:
            # extraemos las partes numericos de los numeros que comparten palabras
            # por ejemplo '3.2' de '3.2 billion'
            parte_numerica = ki_limpio.replace(palabra, "").strip()
            try:
                #se usa el float en caso de que haya decimales
                return int(float(parte_numerica) * valor)
            except:
                return 0

    #si es un entero ya sin puntos ni comas, retornamos:
    try:
        return int(ki_limpio)
    except ValueError:
        return 0

endpoint = "https://dragonball-api.com/api/characters?limit=58"

try:
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()

    diccRazas = dict() # diccionario vacio para manejar la info

    for character in data['items']:
        #Almacenamos los datos necesarios en estas variables
        raza = character['race']
        nombre = character['name']
        ki = limpiar_ki(character['ki']) #Procesamos el ki retornado por la api

        if raza not in diccRazas:
            diccRazas[raza] = []
        diccRazas[raza].append({ #Guardamos la info del nombre y el ki por raza
            "nombre": nombre, 
            "ki": ki
            })
        
    # CALCULO DE PROMEDIOS
    for razas, personajes in diccRazas.items():
        suma_ki_raza = 0 #inicializamos la suma de ki a cero
        #Imprimos las razas con sus respectivos personajes y ki en formato "tabla"
        print(f"{"-"*12} RAZA: {razas.upper()} {"-"*12}")
        print(f"NOMBRE: \t\tKI")

        #Imprimimos el nombre y el ki por cada personaje
        for personaje in personajes:
            print(f"{personaje['nombre']}: \t\t{personaje['ki']:,.2f}")
            suma_ki_raza += personaje['ki'] # acumulamos el ki de cada personaje

        promedio_ki_raza = suma_ki_raza / len(personajes) #calculamos el promedio por raza
        print(f"Promedio de Ki: {promedio_ki_raza:,.2f} \n")

except requests.exceptions.RequestException as e:
    print(f"Error recuperando la data: {e}")