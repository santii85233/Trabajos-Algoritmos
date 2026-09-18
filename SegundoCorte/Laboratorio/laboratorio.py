import copy
import time
laberinto = [
    [0, 0, 1, 0, 0],
    [0, 1, 2, 1, 0],    #los puntos de acopio estan marcados por el numero 2
    [0, 1, 2, 1, 0],    #las calles cerradas y sin salida estan marcadas con el numero 1    
    [0, 1, 2, 1, 0],    #las calles abiertas que no tienen un punto de acopio estan marcadas por el numero 0  
    [0, 0, 0, 0, 0],
]
FILAS, COLS = len(laberinto), len(laberinto[0])
camino = [[0] * COLS for _ in range(FILAS)]
visitados = set() # Guarda el estados como (f, c, puntos)
caminosValidos = []
puntosAcopio = 0
longitudMenor = 0
contador = 0
pasosActuales = 0  # cuenta los pasos reales del recorrido actual
for filas in laberinto:
    for i in range(len(filas)):
        if filas[i] == 2:
            puntosAcopio += 1

def resolver(f, c, puntosAcopio):
    global contador, pasosActuales
    # 1. ¿me sali del tablero?
    if f < 0 or f >= FILAS or c < 0 or c >= COLS:
        return False
    # 2. ¿es muro?
    if laberinto[f][c] == 1:
        return False
    # Calcula cuantos puntos tendría al pisar esta casilla
    es_nuevo_acopio = (laberinto[f][c] == 2 and camino[f][c] == 0)
    estado_futuro = contador + (1 if es_nuevo_acopio else 0)
    # Crea el estado (x, y, puntos)
    estado_actual = (f, c, estado_futuro)
    # ¿Ya pase por aqui con la misma cantidad de puntos?
    if estado_actual in visitados:
        return False
    # 3. Marca esta casilla como parte del camino y registra el estado
    if es_nuevo_acopio:
        contador += 1
    visitados.add(estado_actual) # Guardo el estado en la memoria
    valor_anterior = camino[f][c]
    if laberinto[f][c] == 2:
        camino[f][c] = 2
    else:
        camino[f][c] = 1
    pasosActuales += 1  # un paso mas en este recorrido
    # 4. CASO BASE: llegue a la salida
    if f == FILAS - 1 and c == COLS - 1 and puntosAcopio == contador:
        caminosValidos.append((pasosActuales, copy.deepcopy(camino)))  # guarda los pasos
        # Backtracking
        pasosActuales -= 1
        visitados.remove(estado_actual)
        camino[f][c] = valor_anterior
        if es_nuevo_acopio:
            contador -= 1
        return False
    # 5. CASO RECURSIVO: prueba las cuatro direcciones
    resolver(f + 1, c, puntosAcopio)
    resolver(f, c + 1, puntosAcopio)
    resolver(f - 1, c, puntosAcopio)
    resolver(f, c - 1, puntosAcopio)
    # 6. BACKTRACKING desmarca, borra el estado y se devuelve
    pasosActuales -= 1 
    visitados.remove(estado_actual) # Quita el estado de la memoria
    camino[f][c] = valor_anterior
    if es_nuevo_acopio:
        contador -= 1
    return False
inicio = time.perf_counter()
resolver(0, 0, puntosAcopio)
final = time.perf_counter()
duracion = final - inicio
if caminosValidos != []:
    print(f"Hay salida. Caminos validos encontrados: {len(caminosValidos)}")
    for pasos, caminos in caminosValidos:  # desempaqueta pasos y grilla
        if longitudMenor == 0 or longitudMenor > pasos:  #compara pasos directamente
            longitudMenor = pasos
            caminoFinal = caminos
    print(f"El camino mas corto tiene {longitudMenor} pasos")
    for f in range(FILAS):
        print("  " + " ".join(
            "*" if caminoFinal[f][c] == 1 else (
                "#" if laberinto[f][c] == 1 else (
                    "p" if caminoFinal[f][c] == 2 else "."
                )
            ) for c in range(COLS)
        ))
else:
    print("No hay salida.")
print(f"La funcion tardo: {duracion} segundos en completarse")


"""
 *PARTE A: ¿Cuántos caminos distintos encontró el algoritmo?

 El algoritmo encuentra un número muy elevado de rutas .
 Esto pasa porque el estado guardado incluye los puntos acumulados, permitiendo que
 el algoritmo re-visite casillas y alterne el orden de recolección de los puntos 
 entre las ramas izquierda y derecha.
 
 *PARTE B: ¿Qué pasa con el tiempo de ejecución al pasar de 5x5 a 10x10?

 El tiempo de ejecución se desborda exponencialmente y el programa se congela no deja ni ejecutarlo.
 Esto pasa porque la busqueda explora todas las combinaciones de caminos y estados de recolección posibles, 
 elevando asi la forma en que las puede llegar a calcular en un 10X10.
 
 *PARTE C: Por qué este problema no se puede resolver con ciclos anidados:
 
 1. Los ciclos anidados solo permiten recorridos unidireccionales y estáticos sobre la matriz.
 2. Un laberinto exige explorar múltiples ramas dinámicas y retroceder (backtracking) al toparse con muros.
 3. La recolección de puntos altera el estado del sistema, habilitando re-visitar celdas previamente 
 transitadas aumentando los casos de visita exponencialmente."""
