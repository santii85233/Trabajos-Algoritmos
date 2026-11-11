#Reto 2
class Nodo():
    def __init__(self,clave):
        self.clave = clave
        self.izq = None
        self.der = None

def alt(n):return -1 if n is None else n.alt
def fe(n):return 0 if n is None else alt(n.izq) - alt(n.der)
def recalc(n):n.alt = 1 + max(alt(n.izq), alt(n.der))

def insertar(n, clave):
    if n is None: return Nodo(clave)
    if clave < n.clave: n.izq = insertar(n.izq, clave)
    if clave > n.clave: n.der = insertar(n.der, clave)
    recalc(n)                      # único cambio: se guarda la altura
    return n

def contar(disponible, actual, c):
    if not disponible:
        r = None
        for k in actual: r = insertar(r, k)
        if alt(r) == 2: c[0] += 1
        if alt(r) == 6: c[1] += 1
        return
    for i in range(len(disponible)):
        actual.append(disponible[i])
        contar(disponible[:i]+disponible[i+1:], actual, c)
        actual.pop()

c = [0, 0]
contar([1,2,3,4,5,6,7], [], c)
print("altura 2:", c[0], " altura 6:", c[1])

"""

El mejor orden es  4, 2, 6, 1, 3, 5, 7 
que tiene una altura de 2 y todos los fe estan en 0.
Por otro lado, el peor orden es 1, 2, 3, 4, 5, 6, 7 
que da altura 6 y fe desde -6 hasta 0.

Qué tienen en común los órdenes de altura 2:

Todos empiezan por el 4.
notese que en cada mitad pasa lo mismo de que el 2 debe llegar antes que el 1 y el 3,
y el 6 antes que el 5 y el 7.

Cuántos son: 7! / (7·3·3·1·1·1·1) = 5040 / 63 = 80. Es decir, solo el 80 de los 5040 órdenes da el árbol perfecto. 
Los de altura 6 son 2⁶ = 64, porque en cada paso se elige el menor o el mayor de los que quedan.
"""