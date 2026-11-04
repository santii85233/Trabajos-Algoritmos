# Sesion 40 — Grafos: matriz de adyacencia frente a lista de adyacencia

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
    [8, 1],  # Vereda -> Norte
    [7, 5],  # Bosa -> Chapinero
    [5, 8],  # Chapinero -> Vereda
    [2, 6],  # Sur -> Usaquen
    [6, 8],  # Usaquen -> Vereda
    [5, 2],  # Chapinero -> Sur
    ]
N = 9

# ---------- Representacion 1: matriz de adyacencia ----------
matriz = [[0]*N for _ in range(N)]
for u, v in ARISTAS:
    matriz[u][v] = 1
    matriz[v][u] = 1              # grafo NO dirigido: la matriz es simetrica

print("MATRIZ DE ADYACENCIA")
print("            " + " ".join(f"{n[:3]:>4}" for n in NOMBRES))
for i in range(N):
    print(f"{NOMBRES[i]:>11} " + " ".join(f"{matriz[i][j]:>4}" for j in range(N)))

# ---------- Representacion 2: lista de adyacencia ----------
lista = [[] for _ in range(N)]
for u, v in ARISTAS:
    lista[u].append(v)
    lista[v].append(u)
for v in lista: v.sort()

print("\nLISTA DE ADYACENCIA")
for i in range(N):
    print(f"  {NOMBRES[i]:>10} -> {', '.join(NOMBRES[j] for j in lista[i])}")

# ---------- Grados ----------
print("\nGRADO DE CADA VERTICE (cuantas vias salen de el)")
for i in range(N):
    g_mat = sum(matriz[i])        # recorrer una fila: O(N)
    g_lis = len(lista[i])         # leer el tamano: O(1)
    assert g_mat == g_lis
    print(f"  {NOMBRES[i]:>10}: {g_lis}")

# ---------- Costos ----------
aristas = len(ARISTAS)
print(f"\nV = {N} vertices,  E = {aristas} aristas")
print(f"  Matriz : {N*N} casillas en memoria. ¿Existe arista? O(1). Recorrer vecinos: O(V) = {N} casillas.")
print(f"  Lista  : {2*aristas} referencias en memoria. ¿Existe arista? O(grado). Recorrer vecinos: O(grado).")
densidad = 2*aristas / (N*(N-1))
print(f"  Densidad = 2E / (V(V-1)) = {densidad:.2f}  ->  grafo {'DENSO: conviene matriz' if densidad > 0.5 else 'DISPERSO: conviene lista'}")

# ---------- Consulta de arista ----------
def hay_via_matriz(u, v): return matriz[u][v] == 1
def hay_via_lista(u, v):  return v in lista[u]
for u, v in [(1,0),(1,8),(5,6)]:
    print(f"  ¿{NOMBRES[u]} conecta con {NOMBRES[v]}? matriz={hay_via_matriz(u,v)}  lista={hay_via_lista(u,v)}")
