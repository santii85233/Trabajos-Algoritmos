from collections import deque
NOMBRES = ["CALC1","CALC2","CALC3","ALGEBRA","ECUDIF","FIS1","FIS2",
           "PROG1","PROG2","ESTDAT","ALGO","BD"]
N = len(NOMBRES)
dic = {n: i for i, n in enumerate(NOMBRES)}
PARES = [("CALC1","CALC2"),("CALC2","CALC3"),("CALC2","ECUDIF"),
         ("CALC3","ECUDIF"),("ALGEBRA","ECUDIF"),("CALC1","ALGEBRA"),
         ("CALC1","FIS1"),("FIS1","FIS2"),("CALC2","FIS2"),
         ("PROG1","PROG2"),("PROG2","ESTDAT"),("ESTDAT","ALGO"),
         ("ALGEBRA","ALGO"),("PROG2","BD"),("ESTDAT","BD")]

def armar_lista(pares):
    l = [[] for _ in range(N)]
    for a, b in pares: l[dic[a]].append(dic[b])
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


def ruta(origen, destino):
    ori, dest = dic[origen], dic[destino]
    if ori == dest:
        return f"{origen} -> {destino}: ya estas en el destino (0 tramos)."
    _, dist, padre = bfs(ori, lista)
    if dist[dest] == -1:                               # el caso sin camino
        return f"No hay ruta de {origen} a {destino} (siguiendo el sentido de los prerrequisitos)."
    return f"{' -> '.join(camino(dest, padre))}  ({dist[dest]} tramos)"

print(ruta("CALC1", "ECUDIF"))      # ruta normal
print(ruta("PROG2", "PROG2"))       # origen = destino
print(ruta("ECUDIF", "CALC1"))      # inalcanzable
print(ruta("FIS2", "BD"))           # inalcanzable