""""
fe +2 LL rotacion derecha
fe -2 RR rotacion izquierda
fe -1 LR rotacion izquierda sobre el hijo
fe -1 LR rotacion izquierda sobre el hijo

# fe > 0  -> pesa la izquierda
# fe < 0  -> pesa la derecha
# |fe| > 1 -> hay que rotar

"""
class Nodo():
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None 

def alt(n):return -1 if n is None else n.alt      # arbol vacio: -1

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
def ver(titulo,raiz):
    s=[]; preorden(raiz,s)
    t=[]; inorden(raiz,t)
    print(f"{titulo:22s} preorden: {''.join(s)}")
    print(f"{'':22s} inorden: {t} altura={alt(raiz)}")

print("CASO LL  (pesado a la izquierda-izquierda)  ->  una rotacion DERECHA")
r = Nodo(30); r.izq = Nodo(20); r.izq.izq = Nodo(10)
for n in (r.izq.izq, r.izq, r): recalc(n)
ver("antes (fe raiz = 2)", r); r = rotarDerecha(r); ver("despues", r)

print("\nCASO RR  (pesado a la derecha-derecha)      ->  una rotacion IZQUIERDA")
r = Nodo(10); r.der = Nodo(20); r.der.der = Nodo(30)
for n in (r.der.der, r.der, r): recalc(n)
ver("antes (fe raiz = -2)", r); r = rotarIzquierda(r); ver("despues", r)

print("\nCASO LR  (izquierda-derecha)  ->  IZQUIERDA sobre el hijo, luego DERECHA sobre la raiz")
r = Nodo(30); r.izq = Nodo(10); r.izq.der = Nodo(20)
for n in (r.izq.der, r.izq, r): recalc(n)
ver("antes (fe raiz = 2)", r)
r.izq = rotarIzquierda(r.izq); recalc(r); ver("tras rotar el hijo", r)
r = rotarDerecha(r); ver("despues", r)

print("\nCASO RL  (derecha-izquierda) ->  DERECHA sobre el hijo, luego IZQUIERDA sobre la raiz")
r = Nodo(10); r.der = Nodo(30); r.der.izq = Nodo(20)
for n in (r.der.izq, r.der, r): recalc(n)
ver("antes (fe raiz = -2)", r)
r.der = rotarDerecha(r.der); recalc(r); ver("tras rotar el hijo", r)
r = rotarIzquierda(r); ver("despues", r)