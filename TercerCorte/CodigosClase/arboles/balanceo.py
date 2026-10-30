def alt(n):
    return -1 if n is None else n.alt      # arbol vacio: -1

def fe(n):                                  # factor de equilibrio
    return 0 if n is None else alt(n.izq) - alt(n.der)

def recalc(n):
    n.alt = 1 + max(alt(n.izq), alt(n.der))

# fe > 0  -> pesa la izquierda
# fe < 0  -> pesa la derecha
# |fe| > 1 -> hay que rotar