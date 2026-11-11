
def matrizALista(m):
    return [[j for j in range(len(m)) if m[i][j] == 1] for i in range(len(m))]

def listaAMatriz(l):
    n = len(l)
    m = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in l[u]: m[u][v] = 1
    return m


NOMBRES = ["CALC1", "CALC2", "CALC3", "ECUDIF"]
# CALC1 -> CALC2, CALC2 -> CALC3, CALC2 -> ECUDIF, CALC3 -> ECUDIF
m = [[0, 1, 0, 0],
     [0, 0, 1, 1],
     [0, 0, 0, 1],
     [0, 0, 0, 0]]

l = matrizALista(m)
print(l)                       # [[1], [2, 3], [3], []]

m2 = listaAMatriz(l)
print(m2 == m)                 # True
print(listaAMatriz(matrizALista(m)))