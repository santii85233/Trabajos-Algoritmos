class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None

def esBST(n, minimo=float('-inf'), maximo=float('inf')):
    if n is None:   return True # Caso base    
    if not (minimo < n.clave < maximo):     return False     # Comprobar si la clave actual está dentro del rango permitido
    return esBST(n.izq, minimo, n.clave) and esBST(n.der, n.clave, maximo)

# Raíz: 50
# Hijo izquierdo: 30
# Hijo derecho de 30: 60 (está en la izquierda de 50 pero es mayor que 50)
raiz_falsa = Nodo(50)
raiz_falsa.izq = Nodo(30)
raiz_falsa.izq.der = Nodo(60)

resultado = esBST(raiz_falsa)
print("Resultado del contraejemplo:", resultado)