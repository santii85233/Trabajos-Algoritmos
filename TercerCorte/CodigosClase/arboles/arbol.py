"""
Arbol es una estructura no lineal que permite 
almacenar datos de manera jerarquica.
Cada elemento del árbol se llama nodo, 
y cada nodo puede tener cero o mpas nodos hijos.
El nodo superior se llama raíz,
y los nodos sin hijos se llaman hojas.
Raiz:   Nodo principal del árbol
Nodo: Elemento del arbol que almacena datos
y puede tener hijos.
-----------------------------------------------
Padre-hijo: Relación de nodos, donde un nodo padre tiene uno o más nodos hijos.

hojas: Nodos sin hijos.
aristas: Uniones entre nodos, representan la relación padre-hijo.

arbol: cada nodo puede tenre un numero variable de hijos
binario: cada nodo puede tener como mázimo dos hijos
busqueda binaria: arbol binario con la propiedad de que para cada nodo
 todos los valores en el subarbol izquierdo son menores que el valor del nodo, y
 todos los valores en el sub arbol derecho son mayores que el valor del nodo.

 arboles de decision:   son utilizados para el aprendizaje 
 automatico para tomar decisiones basadas en las caracteristicas de los datos.
 Son modelos predictivos  
"""
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