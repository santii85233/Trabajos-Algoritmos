# Función para convertir una lista de números en un nombre (A=1 ... Z=26)
def obtener_nombre(numeros):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    # El índice en Python empieza en 0, por eso restamos 1
    return "".join(abecedario[n-1] for n in numeros).capitalize()

# Diccionario con las listas de números asignadas a cada casillero
datos_casilleros = {
    "casillero1": [19, 5, 18, 7, 9, 15],       # Sergio 
    "casillero2": [19, 1, 14, 20, 9, 1, 7, 15], # Santiago
    "casillero3": [10, 21, 12, 9, 1, 14],      # Julian 
    "casillero4": [14, 9, 3, 15, 12, 1, 19],    # Nicolas
    "casillero5": [1, 19, 9, 5, 18],            # Asier
    "casillero6": [15, 19, 3, 1, 18],           # Oscar
    "casillero7": [1, 14, 4, 18, 5, 19],        # Andres
    "casillero8": [13, 1, 18, 9, 1],            # Maria
    "casillero9": [5, 19, 20, 5, 2, 1, 14],     # Esteban
    "casillero10": [5, 4, 23, 1, 18, 4],        # Edward
    "casillero11": [4, 1, 14, 9, 5, 12]         # Daniel
}

# Impresión de los resultados con su respectivo nombre descifrado
for llave, numeros in datos_casilleros.items():
    nombre_persona = obtener_nombre(numeros)
    suma = sum(numeros)
    resultado = suma % 11
    
    print(f"{llave.capitalize():<12} | Nombre: {nombre_persona:<9} | Suma: {suma:<3} | Resultado % 11 = {resultado}")

"""El casillero que mas tiene es el 1 contando con 3 asignaciones que son Julian, Oscar y Daniel

3.Si quisieramos buscar a edward lo podriamos encontrar buscando el residuo de lo que dio el resultado.

"""