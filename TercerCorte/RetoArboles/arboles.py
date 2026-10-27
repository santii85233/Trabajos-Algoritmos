class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def preorden(n, salida):
    if n is None: return          # caso base: subarbol vacio
    salida.append(n.dato)         # 1) raiz
    preorden(n.izq, salida)       # 2) izquierda
    preorden(n.der, salida)       # 3) derecha

def inorden(n, salida):
    if n is None: return
    inorden(n.izq, salida)        # 1) izquierda
    salida.append(n.dato)         # 2) raiz
    inorden(n.der, salida)        # 3) derecha

def postorden(n, salida):
    if n is None: return
    postorden(n.izq, salida)      # 1) izquierda
    postorden(n.der, salida)      # 2) derecha
    salida.append(n.dato)         # 3) raiz

def altura(n):
    if n is None: return -1       # arbol vacio: altura -1 (un solo nodo: 0)
    return 1 + max(altura(n.izq), altura(n.der))

def contar(n):
    if n is None: return 0
    return 1 + contar(n.izq) + contar(n.der)

def contar_hojas(n):
    if n is None: return 0
    if n.izq is None and n.der is None: return 1
    return contar_hojas(n.izq) + contar_hojas(n.der)

def por_niveles(raiz):
    if raiz is None: return []
    from collections import deque
    cola = deque([raiz]); salida = []
    while cola:
        n = cola.popleft()
        salida.append(n.dato)
        if n.izq: cola.append(n.izq)
        if n.der: cola.append(n.der)
    return salida

#RETO1
def imprimir_jerarquia(n, nivel=0):
    if n is None: return  #Caso bse de un arbol vacio
    print("  " * nivel + n.dato) #Imprime la raíz con doble espacio * nivel
    # Recorre los hijos (preorden)
    imprimir_jerarquia(n.izq, nivel + 1)
    imprimir_jerarquia(n.der, nivel + 1)

#RETO2
def espejo(n):
    if n is None: return #CASO BASE
    espejo(n.izq) #recursivo izq
    espejo(n.der) #recursivo der
    n.izq, n.der = n.der, n.izq #cambio de valores en los nodos 

#Reto3
def sonIguales(a,b):
    if a is None and b is None: return True #Los dos son vacios
    if a is None or b is None: return False #uno es vacio y el otro no
    if a.dato != b.dato: return False #sus datos raiz son diferentes
    return sonIguales(a.izq, b.izq) and sonIguales(a.der,b.der) # si tiene hijos verifica que sean iguales


raiz = Nodo("CATALOGO")
raiz.izq = Nodo("HERRAMIENTA"); raiz.der = Nodo("LIBRO")
raiz.izq.izq = Nodo("TALADRO");  raiz.izq.der = Nodo("SIERRA")
raiz.der.izq = Nodo("ARTE");     raiz.der.der = Nodo("TECNICO")
raiz.der.der.der = Nodo("REDES")


raiz1 = Nodo("CATALOGO")
raiz1.izq = Nodo("HERRAMIENTA"); raiz1.der = Nodo("LIBRO")
raiz1.izq.izq = Nodo("TALADRO");  raiz1.izq.der = Nodo("SIERRA")
raiz1.der.izq = Nodo("ARTE");     raiz1.der.der = Nodo("TECNICO")
raiz1.der.der.der = Nodo("REDES")

#Prueba Reto3
if sonIguales(raiz,raiz1): print("Los árboles son iguales")
else: print("Los árboles son diferentes")

#Prueba Reto2 y Reto1
#Inorder del arbol original
salida_original = []
inorden(raiz, salida_original)
print("Inorden original:", salida_original)
imprimir_jerarquia(raiz)

#Inorder del espejo
espejo(raiz)
salida_espejo = []
inorden(raiz, salida_espejo)
print("Inorden del espejo: ", salida_espejo)
imprimir_jerarquia(raiz)

#Prueba Reto3 despues de hacer espejo a raiz original
if sonIguales(raiz,raiz1): print("Los árboles son iguales")
else: print("Los árboles son diferentes")




