"""Un arbol binario de busqueda es un arbol que cumple en todos sus nodos
que todas las claves del subarbol izquierdo deben ser menores que
las claves del nodo y todas las del derecho deben ser mayores que las del nodo.


-arbol con inorden no se tiene que ordenar y tiene complejidad O(n)



"""
from arbol import *

def insertar(n,clave):
    if n is None:
        return Nodo(clave)
    if clave < n.clave:
        n.izq = insertar(n.izq,clave)
    if clave > n.clave:
        n.der = insertar(n.der,clave)
    return n

#eliminar nodo (hoja)
#eliminar nodo (con un hijo): El hijo sube a ocupar el lugar del padre y el subarbol se reengancha al abuelo
#el nodo tiene dos hijos se busca un sucesor inorden(minimo del subarbol derecho) se copia la clave en el nodo
#y se elimina el sucesor inorden
def eliminar(n,clave):
    pass