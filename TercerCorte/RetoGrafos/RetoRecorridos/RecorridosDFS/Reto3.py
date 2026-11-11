"""
El camino más corto es fácil porque BFS marca cada vertice una sola vez 
y esa marca es definitiva ya que la primera vez que se llega a un vértice
es por el camino más corto, y el camino a un vértice se construye extendiendo
el camino más corto a su padre. Todo cuesta O(V+E).
Con el camino más largo eso no funciona ya que un vértice usado por 
un camino puede ser necesario para otro mejor, así que no se puede marcar
como visitado para siempre y hay que desmarcarlo al regresar (backtracking). 
Eso obliga a revisar todos los caminos simples posibles, donde su numero crece de forma exponencial."""


from collections import deque
import time, sys


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

sys.setrecursionlimit(10000)
def mas_largo(u, destino, lista, visitado, ruta, mejor):
    if u == destino:
        if len(ruta) > len(mejor[0]): mejor[0] = ruta[:]
        return
    for v in lista[u]:
        if not visitado[v]:
            visitado[v] = True; ruta.append(v)    # marcar
            mas_largo(v, destino, lista, visitado, ruta, mejor)
            ruta.pop(); visitado[v] = False       # DESMARCAR al regresar

def largo(n, aristas):
    lista = [[] for _ in range(n)]
    for a, b in aristas: lista[a].append(b); lista[b].append(a)
    vis = [False] * n; vis[0] = True; mejor = [[]]
    t = time.perf_counter()
    mas_largo(0, n - 1, lista, vis, [0], mejor)
    return len(mejor[0]) - 1, time.perf_counter() - t

def red_prueba(n, k=3):     # cada vértice se une con los 3 siguientes
    return n, sorted({(i, (i + d) % n) for i in range(n) for d in range(1, k + 1)})

for n in (9, 15, 20):
    nn, a = red_prueba(n)
    L, seg = largo(nn, a)
    print(f"V={nn:2d} aristas={len(a):2d} tramos={L:2d} tiempo={seg:.4f} s")
