#BST 50,30,70,20,40,60,80 Y 35
#Medir cuantos hijos tiene cada nodo antes de eliminar

#Salida inorden: [20, 30, 35, 40, 50, 60, 70, 80]

from arbol import *

def insertar(n, clave, nombre=""):
    if n is None: return Nodo(clave, nombre)
    if clave < n.clave: n.izq = insertar(n.izq, clave, nombre)
    if clave > n.clave: n.der = insertar(n.der, clave, nombre)
    return n

def buscar(n,clave,pasos=None):
    if pasos is not None: pasos.append("vacio" if n is None else str(n.clave))
    if n is None or (n.clave == clave): return n
    return buscar(n.izq, clave, pasos)if clave < n.clave else buscar(n.der, clave, pasos)

def minimo(n):
    while n.izq is not None: n = n.izq
    return n
def maximo(n):
    while n.der is not None: n = n.der
    return n

def eliminar(n, clave):
    if n is None: return None
    if clave < n.clave: n.izq = eliminar(n.izq, clave)
    elif clave > n.clave: n.der = eliminar(n.der, clave)
    else:
        if n.izq is None: return n.der
        if n.der is None: return n.izq
        sucesor = minimo(n.der)
        n.clave = sucesor.clave
        n.nombre = sucesor.nombre
        n.der = eliminar(n.der, sucesor.clave)
    return n

def altura(n):
    if n is None: return -1
    return 1 + max(altura(n.izq), altura(n.der))

def inorden(n, salida):
    if n is None: return
    inorden(n.izq, salida)
    salida.append(n.clave)
    inorden(n.der, salida)
raiz = None
for clave in [50, 30, 70, 20, 40, 60, 80, 35]:
    raiz = insertar(raiz, clave)
s=[];inorden(raiz, s); print("queda ordenado",s)