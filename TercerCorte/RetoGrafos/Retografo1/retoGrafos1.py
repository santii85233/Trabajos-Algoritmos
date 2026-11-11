NOMBRES = ["CALC1","CALC2","CALC3","ALGEBRA","ECUDIF","FIS1","FIS2",
           "PROG1","PROG2","ESTDAT","ALGO","BD"]
N = len(NOMBRES)
dic = {nombre: i for i, nombre in enumerate(NOMBRES)} #Indice a cada materia

#Aristas de las materias
ARISTAS = [("CALC1","CALC2"),("CALC2","CALC3"),("CALC2","ECUDIF"),
           ("CALC3","ECUDIF"),("ALGEBRA","ECUDIF"),("CALC1","ALGEBRA"),
           ("CALC1","FIS1"),("FIS1","FIS2"),("CALC2","FIS2"),
           ("PROG1","PROG2"),("PROG2","ESTDAT"),("ESTDAT","ALGO"),
           ("ALGEBRA","ALGO"),("PROG2","BD"),("ESTDAT","BD")]


ARISTAS = [(dic[a], dic[b]) for a, b in ARISTAS] # crea las posiciones de las aristas con sus indices


# se hace una matriz DIRIGIDA, solo [u][v]
matriz = [[0] * N for _ in range(N)]
for u, v in ARISTAS:
    matriz[u][v] = 1

# lista hacia solo una dirección
lista = [[] for _ in range(N)]

for u, v in ARISTAS:
    lista[u].append(v) #se agregan los prerequisitos a cada materia
for vecinos in lista: vecinos.sort() #Se ordena

def hay_via(u, v): return matriz[u][v] == 1          # dice si u es prerequisito de b

simetrica = all(matriz[i][j] == matriz[j][i] for i in range(N) for j in range(N)) #REVISA si matriz[i][j] es igual a matriz[j][i]
print("¿Matriz simétrica?", simetrica)               # False, puesto que es un grafo dirigido

gradoSalida = [sum(fila) for fila in matriz]
gradoEntrada = [sum(matriz[i][j] for i in range(N)) for j in range(N)]
assert gradoSalida == [len(l) for l in lista]              # coinciden por los dos caminos

E = len(ARISTAS)
densidad = E / (N * (N - 1))      # dirigido: máximo V(V-1)
print(f"V={N} E={E} densidad={densidad:.3f}")        # 0.114