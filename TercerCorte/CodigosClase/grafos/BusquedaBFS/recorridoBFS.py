#Quiz colores 6/11
from collections import deque

NOMBRES = ["CENTRO","NORTE","SUR","ORIENTE","OCCIDENTE",
                    "CHAPINERO","USAQUEN","BOSA","VEREDA"]
ARISTAS = [[0, 1],  # Centro -> Norte
    [1, 4],  # Norte -> Occidente
    [0, 2],  # Centro -> Sur
    [0, 3],  # Centro -> Oriente
    [1, 5],  # Norte -> Chapinero
    [2, 7],  # Sur -> Bosa
    [3, 6],  # Oriente -> Usaquen
    [5, 6],  # Chapinero -> Usaquen
    [4, 7],  # Occidente -> Bosa
    [7, 8],  # Bosa -> Vereda
    [7, 5],  # Bosa -> Chapinero
    [5, 8],  # Chapinero -> Vereda
    [2, 6],  # Sur -> Usaquen
    [6, 8],  # Usaquen -> Vereda
    [5, 2],  # Chapinero -> Sur
    ]
N = 9

lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    lista[u].append(v); lista[v].append(u)
for v in lista: v.sort()

def bfs(inicio):
    visitado = [False] * N
    dist  = [-1] * N          # distancia en numero de tramos
    padre = [-1] * N          # de donde llegue: permite reconstruir el camino
    cola = deque([inicio])
    visitado[inicio] = True   # se marca al ENCOLAR, no al sacar
    dist[inicio] = 0
    orden = []
    while cola:
        u = cola.popleft()    # FIFO: sale el primero que entro
        orden.append(u)
        for v in lista[u]:
            if not visitado[v]:
                visitado[v] = True
                dist[v]  = dist[u] + 1
                padre[v] = u
                cola.append(v)
    return orden, dist, padre

print("\nBFS ITERATIVO desde CENTRO")
orden, distancias, padres = bfs(0)
print((orden, distancias, padres))

#CAMINO MAS CORTO HASTA VEREDA DESDE CENTRO 
destino = 8  # VEREDA
camino = []
actual = destino
while actual != -1:
    camino.append(actual)
    actual = padres[actual]
    print(camino)
camino.reverse()
for n in range(len(NOMBRES)):
    AZUL = "\033[34m"
    VERDE = "\033[32m"
    ROJO = "\033[31m"
    BLANCO = "\033[37m"
    RESET = "\033[0m"  # Importante para que el color no se "falle" a las siguientes líneas

    if distancias[n] == 0:
        print(f"{AZUL}Nivel 0: {NOMBRES[n]}{RESET}")

    elif distancias[n] == 1:
        print(f"{VERDE}Nivel 1: {NOMBRES[n]}{RESET}")

    elif distancias[n] == 2:
        print(f"{ROJO}Nivel 2: {NOMBRES[n]}{RESET}")

    elif distancias[n] == 3:
        print(f"{BLANCO}Nivel 3: {NOMBRES[n]}{RESET}")

print("\nCAMINO MAS CORTO HASTA VEREDA DESDE CENTRO:")
print(f"Distancia (tramos): {distancias[destino]}")
nombres_coloreados = []
COLORES = {
    0: "\033[34m",  # Azul
    1: "\033[32m",  # Verde
    2: "\033[31m",  # Rojo
    3: "\033[37m"   # Blanco
}
RESET = "\033[0m"

for i in camino:
    nivel = distancias[i]
    color = COLORES.get(nivel, "")  # Toma el color del nivel, o vacío si no existe
    nombres_coloreados.append(f"{color}{NOMBRES[i]}{RESET}")

# Imprimimos la ruta uniendo los nombres ya coloreados
print("Ruta:", " -> ".join(nombres_coloreados))

