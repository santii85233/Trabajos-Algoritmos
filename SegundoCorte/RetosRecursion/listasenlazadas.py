# Definición de un Nodo de lista enlazada
class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


# RETO 4: Recorrido e impresión inversa
def imprimirInverso(nodo):
    if nodo is None:  # Caso Base, llegamos al final de la lista enlazada
        return
    else:
        # Hacemos la llamada recursiva PRIMERO hacia el siguiente nodo
        imprimirInverso(nodo.siguiente)

        # Imprimimos DESPUÉS de volver de la llamada
        print(nodo.valor)


# --- Creación de la lista enlazada
cabeza = Nodo(1)
cabeza.siguiente = Nodo(2)
cabeza.siguiente.siguiente = Nodo(3)
cabeza.siguiente.siguiente.siguiente = Nodo(4)
cabeza.siguiente.siguiente.siguiente.siguiente = Nodo(5)

# Prueba del RETO 4
imprimirInverso(cabeza)