def binaria(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if v[medio] == x:   return medio
        elif v[medio] < x:  izq = medio + 1   # descarto la mitad izquierda
        else:               der = medio - 1   # descarto la mitad derecha
    return -1

#Definir binaria recursiva (Reto1)
def binaria_rec(v, x, izq, der):
    mitad = (izq+der)//2 #Mitad del vector

    #Devuelve la posición donde debería ir el elemento (Reto2)
    if izq > der: return mitad+1 

    # Elimina la mitad derecha Y si se repite el elemento, devuelve la primera posición (Reto3)
    if x <= v[mitad]: return binaria_rec(v,x,izq, mitad-1)

    #Elimina la mitad izquierda
    if x > v[mitad]: return binaria_rec(v,x,mitad+1,der)    


v=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
   41,42,43,44,45,46,47,48,49,50]

p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20]
print("Índice del primer elemento repetido 9 es el:", binaria_rec(v, 9, 0, len(v)-1))
print("Indice donde debe ir el elemento 16 es:", binaria_rec(p, 16, 0, len(p)-1))


