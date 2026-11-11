#Reto 3
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

def caso(n):
    if n is None: return "EQUILIBRADO"
    f = fe(n)
    if f > 1:  return "LL" if fe(n.izq) >= 0 else "LR"
    if f < -1: return "RR" if fe(n.der) <= 0 else "RL"
    return "EQUILIBRADO"


raiz = None
nums =[8, 5, 11, 3, 6, 10, 2, 4, 7, 9, 1]
for k in nums:
    raiz = insertar(raiz, k)
print(nums)
print("fe(11) =", fe(raiz.der), caso(raiz.der))   # 2  LL
print("fe(8)  =", fe(raiz),     caso(raiz))       # 1  EQUILIBRADO

raiz.der = diagnostico(raiz.der)   # rotación correcta
recalc(raiz)
print("fe(8)  =", fe(raiz),     caso(raiz))       # 2  LL
raiz = diagnostico(raiz)           # hace falta una SEGUNDA rotación
