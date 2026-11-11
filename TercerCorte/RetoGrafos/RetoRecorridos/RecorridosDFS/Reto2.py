from collections import deque
NOMBRES = ["CALC1","CALC2","CALC3","ALGEBRA","ECUDIF","FIS1","FIS2",
           "PROG1","PROG2","ESTDAT","ALGO","BD"]
N = len(NOMBRES)
idx = {n: i for i, n in enumerate(NOMBRES)}
PARES = [("CALC1","CALC2"),("CALC2","CALC3"),("CALC2","ECUDIF"),
         ("CALC3","ECUDIF"),("ALGEBRA","ECUDIF"),("CALC1","ALGEBRA"),
         ("CALC1","FIS1"),("FIS1","FIS2"),("CALC2","FIS2"),
         ("PROG1","PROG2"),("PROG2","ESTDAT"),("ESTDAT","ALGO"),
         ("ALGEBRA","ALGO"),("PROG2","BD"),("ESTDAT","BD")]

def armar_lista(pares):
    l = [[] for _ in range(N)]
    for a, b in pares: l[idx[a]].append(idx[b])
    for v in l: v.sort()
    return l
lista = armar_lista(PARES)

def bfs(inicio, lista):                       # el de la sesión 42
    visitado = [False] * N; dist = [-1] * N; padre = [-1] * N
    cola = deque([inicio]); visitado[inicio] = True; dist[inicio] = 0
    orden = []
    while cola:
        u = cola.popleft(); orden.append(u)
        for v in lista[u]:
            if not visitado[v]:
                visitado[v] = True; dist[v] = dist[u] + 1; padre[v] = u
                cola.append(v)
    return orden, dist, padre

def camino(destino, padre):
    ruta = []; v = destino
    while v != -1:
        ruta.append(NOMBRES[v]); v = padre[v]
    return list(reversed(ruta))

PLAN = [("CALC1","CALC2"),("CALC2","CALC3"),("CALC3","ECUDIF"),
        ("ECUDIF","CALC2"),                       # <- ciclo introducido a propósito
        ("ALGEBRA","ECUDIF"),("PROG1","PROG2"),("PROG2","ESTDAT")]
SIN_VISITAR, EN_PROCESO, TERMINADO = 0, 1, 2

def buscar_ciclo(lista):
    estado = [SIN_VISITAR] * N
    pila = []                                     # camino actual
    def dfs(u):
        estado[u] = EN_PROCESO; pila.append(u)
        for v in lista[u]:
            if estado[v] == EN_PROCESO:           # vecino en proceso = ciclo
                return pila[pila.index(v):] + [v]
            if estado[v] == SIN_VISITAR:
                r = dfs(v)
                if r: return r
        pila.pop(); estado[u] = TERMINADO
        return None
    for u in range(N):
        if estado[u] == SIN_VISITAR:
            r = dfs(u)
            if r: return r
    return None

c = buscar_ciclo(armar_lista(PLAN))
print("IMPOSIBLE. Ciclo: " + " -> ".join(NOMBRES[v] for v in c))