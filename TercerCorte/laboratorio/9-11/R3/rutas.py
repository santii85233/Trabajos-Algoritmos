# ============================================================
#  Laboratorio integrador · Corte 3 · RETO 3  (25 puntos)
#  Sesiones 40 y 42 — Representacion de grafos y BFS
#  Sistema: RedAcopio — rutas minimas entre puntos de la red
#
#  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas_r3.py
#  Ejecute:   python3 pruebas_r3.py
# ============================================================
#@SantiagoArteaga
from collections import deque

NOMBRES = ["ACOPIO","NORTE","SUR","ORIENTE","OCCIDENTE",
           "PLANTA","TALLER","PUERTO","VEREDA","MINA"]
ARISTAS = [(0,1),(0,2),(0,3),(1,4),(1,5),(2,7),(3,6),(5,6),(4,7),(7,8),(6,9)]
N = len(NOMBRES)


def construir():
    """Devuelve la lista de adyacencia: una lista de N listas.
       El grafo es NO DIRIGIDO, asi que cada arista se registra en los dos
       extremos. Cada lista de vecinos debe quedar ORDENADA de menor a mayor."""
    ady = [[] for _ in range(N)]
    for u,v in ARISTAS:
        ady[u].append(v)
        ady[v].append(u)
    for vecinos in ady:
        vecinos.sort()
    return ady


def bfs(inicio):
    """Recorrido en anchura desde 'inicio'.
       Devuelve la tupla (orden, dist, padre):
         orden  lista de vertices en el orden en que se atendieron
         dist   dist[v] = numero de tramos desde inicio (-1 si no se alcanza)
         padre  padre[v] = vertice desde el que se llego a v (-1 para el inicio)

       Recuerde: se marca el vertice al ENCOLARLO, no al sacarlo."""

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
        for v in construir()[u]:
            if not visitado[v]:
                visitado[v] = True
                dist[v]  = dist[u] + 1
                padre[v] = u
                cola.append(v)
    return orden, dist, padre

def camino(destino, padre):
    """Ya implementado: reconstruye la ruta siguiendo el arreglo padre."""
    ruta = []
    v = destino
    while v != -1:
        ruta.append(NOMBRES[v])
        v = padre[v]
    return list(reversed(ruta))


def por_niveles(dist):
    """Devuelve una lista de listas: en la posicion d, los NOMBRES de los
       vertices que estan a distancia d del origen."""
    niveles = [[] for _ in range(max(dist)+1)]
    for v, d in enumerate(dist):
        if d!= -1:
            niveles[d].append(NOMBRES[v])
    return niveles
