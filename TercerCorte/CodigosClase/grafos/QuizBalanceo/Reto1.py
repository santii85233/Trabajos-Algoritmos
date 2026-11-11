#QUIZ 30/10
class Nodo():
    def __init__(self,clave):
        self.clave = clave
        self.izq = None
        self.der = None

def insertar(n, clave):
    if n is None: return Nodo(clave)
    if clave < n.clave: n.izq = insertar(n.izq, clave)
    if clave > n.clave: n.der = insertar(n.der, clave)
    return n

def alt(n):return -1 if n is None else 1 + max(alt(n.izq), alt(n.der))     # arbol vacio: -1

def fe(n):return 0 if n is None else alt(n.izq) - alt(n.der) # factor de equilibrio

def recalc(n):n.alt = 1 + max(alt(n.izq), alt(n.der))

def rotarDerecha(y):
    x = y.izq; B = x.der
    x.der = y; y.izq = B # 1) y pasa a ser hijo derecho de x  2) B se cuelga de y
    recalc(y); recalc(x) # 3) primero el que BAJA, luego el que SUBE
    return x             # x es la nueva raiz del subarbol

def rotarIzquierda(x):
    y = x.der;B = y.izq
    y.izq = x; x.der = B
    recalc(x); recalc(y)
    return y

def inorden(n,s):
    if n is None: return
    inorden(n.izq,s); s.append(n.clave);inorden(n.der,s)

def preorden(n,s):
    if n is None: return
    s.append(f"{n.clave}(fe= {fe(n)})");preorden(n.izq,s);preorden(n.der,s); 

def ver(raiz):
    s=[]; preorden(raiz,s)
    t=[]; inorden(raiz,t)
    print(f"{'':22s} preorden: {''.join(s)}")
    print(f"{'':22s} inorden: {t} altura={alt(raiz)}")

def por_niveles(raiz):
    if raiz is None: return []
    from collections import deque
    cola = deque([raiz]); salida = []
    while cola:
        n = cola.popleft()
        salida.append(n.clave)
        if n.izq: cola.append(n.izq)
        if n.der: cola.append(n.der)
    return salida
def imprimir_jerarquia(n, nivel=0):
    if n is None: return  #Caso bse de un arbol vacio
    print("  " * nivel + str(n.clave)) #Imprime la raíz con doble espacio * nivel
    # Recorre los hijos (preorden)
    imprimir_jerarquia(n.izq, nivel + 1)
    imprimir_jerarquia(n.der, nivel + 1)

def diagnostico(raiz):
    if raiz is None: return raiz
    factor = fe(raiz)
    # Caso LL
    if (factor > 1) and fe(raiz.izq) >= 0:return rotarDerecha(raiz)
    # Caso LR
    if (factor > 1) and fe(raiz.izq) < 0:
        raiz.izq = rotarIzquierda(raiz.izq)
        return rotarDerecha(raiz)
    # Caso RR
    if (factor < -1) and fe(raiz.der) <= 0:return rotarIzquierda(raiz)
    # Caso RL
    if (factor < -1) and fe(raiz.der) >= 0:
        raiz.der = rotarDerecha(raiz.der)
        return rotarIzquierda(raiz) 
    return raiz

raiz = None
for n in range(3):
    j = int(input(f"Ingrese la clave {n+1}:"))
    raiz = insertar(raiz, j)

print("\n--- Árbol antes de balancear ---")
ver(raiz)
imprimir_jerarquia(raiz)
print("por niveles", por_niveles(raiz))

raiz = diagnostico(raiz)

print("\n--- Árbol después de balancear ---")
ver(raiz)
imprimir_jerarquia(raiz)
print("por niveles", por_niveles(raiz))