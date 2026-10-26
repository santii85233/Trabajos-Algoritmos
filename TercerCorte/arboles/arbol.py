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
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

raiz = Nodo(10)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(15)