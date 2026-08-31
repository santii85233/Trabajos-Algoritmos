# ============================================================
#  Cívica Software  ·  TCK-4420  ·  Severidad P3
#  Sistema: RedAcopio  —  Reporte de ocupación
#  NO MODIFIQUE la seccion de datos ni el archivo de pruebas.
# ============================================================

# filas = puntos de acopio, columnas = dias de la semana
ocupacion = [
    [4, 2, 6, 1, 3, 0],
    [0, 5, 5, 2, 7, 1],
    [8, 1, 0, 4, 2, 6],
    [3, 3, 3, 0, 0, 5],
]

def total_por_punto(m):
    """Devuelve una lista con el total recogido por cada punto (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def total_por_dia(m):
    """Devuelve una lista con el total recogido cada dia (columna).
       BUG REPORTADO: entrega totales incorrectos."""
    totales = []
    for i in range(len(m[0])):
        s = 0
        for j in range(len(m)):
            s += m[j][i]
        totales.append(s)
    return totales


def dia_mas_flojo(m):
    """Devuelve el indice del dia con MENOR recoleccion total."""
    """Diferencia los dias de la semana y busca el dia con menor recoleccion total."""
    menor = 0 #Inicializa la variable menor con el indice del primer dia (lunes).

    #Hace un recorrido por la lista de totales por dia y compara cada valor con el menor encontrado hasta el momento.
    for i in range(len(total_por_dia(m))):
        #Si el total del dia actual es menor que el total del dia almacenado en la variable menor, actualiza la variable menor con el indice del dia actual.
        if total_por_dia(m)[i] < total_por_dia(m)[menor]:
            menor = i
    #devuelve  el indice  dia con menor recoleccion 
    return menor

def puntos_inactivos(m):
    """Devuelve cuantos registros estan en 0 (el punto no opero ese dia)."""
    contador = 0 #Se inicializa una variable contador en 0 para llevar un registro de la cantidad de registros en 0.
    #Se hace un recorrido por la matriz m, donde i representa el indice de la fila y j representa el indice de la columna.
    for i in range(len(m)):
        for j in range(len(m[i])):
            #Se verifica si el valor en la posición m[i][j] es igual a 0, lo que indica que el punto no operó ese día. Si es así, se incrementa el contador en 1.
            if m[i][j] == 0:
                contador += 1
    return contador

