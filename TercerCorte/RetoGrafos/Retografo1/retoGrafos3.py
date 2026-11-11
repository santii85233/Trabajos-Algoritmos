def existe_regular(V, k):
    pares = [(i, j) for i in range(V) for j in range(i + 1, V)]
    for mascara in range(1 << len(pares)):
        grado = [0] * V
        for b, (i, j) in enumerate(pares):
            if mascara >> b & 1: grado[i] += 1; grado[j] += 1
        if all(g == k for g in grado): return True
    return False


print(existe_regular(5, 3))    # False
print(existe_regular(4, 3))    # True