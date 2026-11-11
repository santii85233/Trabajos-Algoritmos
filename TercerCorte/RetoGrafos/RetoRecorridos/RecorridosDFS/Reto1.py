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


def a_no_dirigida(lista):
    nd = [[] for _ in range(N)]
    for u in range(N):
        for v in lista[u]:
            nd[u].append(v); nd[v].append(u)
    return nd

def dfs_comp(u, nd, comp, c):
    comp[u] = c                          # el índice se asigna durante el recorrido
    for v in nd[u]:
        if comp[v] == -1: dfs_comp(v, nd, comp, c)

def informe(pares, titulo):
    nd = a_no_dirigida(armar_lista(pares))
    comp = [-1] * N; c = 0
    for u in range(N):
        if comp[u] == -1:
            dfs_comp(u, nd, comp, c); c += 1
    zonas = [[NOMBRES[v] for v in range(N) if comp[v] == k] for k in range(c)]
    print(f"\n--- {titulo} ---")
    print(f"La red esta partida en {c} zona{'s' if c != 1 else ''}.")
    for k, z in enumerate(zonas):
        print(f"  Zona {k+1}: {len(z)} materias -> {', '.join(z)}")
    g = max(range(c), key=lambda k: len(zonas[k]))
    print(f"La zona mas grande es la {g+1} con {len(zonas[g])} materias.")
    for k, z in enumerate(zonas):
        if k != g:
            print(f"La zona {k+1} ({len(z)} materias) no tiene conexion con la zona {g+1}.")

informe(PARES, "Red completa")
cortadas = [p for p in PARES if p not in (("CALC1","FIS1"), ("CALC2","FIS2"))]
informe(cortadas, "Tras eliminar CALC1->FIS1 y CALC2->FIS2")