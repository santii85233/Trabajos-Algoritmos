#RETO 1
class Nodo:
    def __init__(self, codigo, nombre, dato):
        self.cod = codigo
        self.nom = nombre
        self.dato = dato
        self.izq = None
        self.der = None

#insertar
def insertar(n, codigo, nombre, dato):
    if n is None: return Nodo(codigo, nombre, dato)
    if codigo < n.cod: n.izq = insertar(n.izq, codigo, nombre, dato)
    elif codigo > n.cod: n.der = insertar(n.der, codigo, nombre, dato)
    return n

def listarOrdenado(n):
    if n is None:
        print("(indice vacio)")
        return
    salida = []
    inorden(n, salida)
    for item in salida:
        print(item)

def inorden(n, salida):
    if n is None: return
    inorden(n.izq, salida)        # 1) izquierda
    salida.append(f"{n.cod}: {n.nom} (Créditos: {n.dato})")  # 2) raiz
    inorden(n.der, salida)        # 3) derecha

# Informe
def informe(n, codigo):
    comparaciones = 0
    actual = n
    while actual is not None:
        comparaciones += 1               
        if codigo == actual.cod:
            print(f"{codigo}: {actual.nom}  ({comparaciones} comparaciones)")
            return actual.nom
        actual = actual.izq if (codigo < actual.cod) else actual.der
    print(f"{codigo}: no encontrado  ({comparaciones} comparaciones)")
    return None

# Demostración
MATERIAS = [  # (codigo, nombre, creditos)
    ("MAT101", "Calculo Diferencial", 4),
    ("FIS201", "Fisica Mecanica", 3),
    ("PROG102", "Programacion Orientada a Objetos", 3),
    ("CAL106", "Calculo 1", 2),
    ("HUM301", "Etica y Sociedad", 2),
    ("FIS105", "Fisica Diferencial", 3),
    ("PROG201", "Estructuras de Datos", 3),
    ("ALG107", "Algebra Lineal", 3),
    ("EST202", "Estadistica", 3),
    ("BD301", "Bases de Datos", 3),
    ("ING101", "Ingles I", 2),
    ("QUI101", "Quimica General", 3),
]

raiz = None
for cod, nom, cred in MATERIAS:
    raiz = insertar(raiz, cod, nom, cred)

print("== listarOrdenado ==")
listarOrdenado(raiz)

print("\n== informe ==")
informe(raiz, "MAT101")    # la raiz
informe(raiz, "QUI101")    # una hoja mas profunda
informe(raiz, "ALG107")    # la izquierda
informe(raiz, "XXX999")    # uno que no existe