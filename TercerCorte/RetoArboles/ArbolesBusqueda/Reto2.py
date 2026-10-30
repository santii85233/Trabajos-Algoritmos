#Reto 2

class Nodo():
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
def insertar(n, clave):
    if n is None: return Nodo(clave)
    if clave < n.clave: n.izq = insertar(n.izq, clave)
    if clave > n.clave: n.der = insertar(n.der, clave)
    return n

def enRango(n, a, b):
    if n is None:   return 0    
    contador = 1
    if a < n.clave:   contador += enRango(n.izq, a, b)
    if a <= n.clave <= b: print(f"{n.clave}")
    if n.clave < b:   contador += enRango(n.der, a, b)
    return contador

raiz = None
for clave in [50, 30, 70, 20, 40, 60, 80, 35]:
    raiz = insertar(raiz, clave)

print("claves en el rango [35, 65]")
total_visitados = enRango(raiz, 35, 65)
print(f"Total de nodos visitados: {total_visitados}")