"""RETO 3  ·  Rotar el plano 90 grados   
Contexto: Un mapa de zonas de reciclaje está guardado como matriz, pero se necesita imprimirlo girado para que coincida con la orientación real del barrio.
Se pide: Escribir una función que reciba una matriz de f filas por c columnas y devuelva una nueva matriz rotada 90 grados en sentido horario. Verificar que [1,2,3],[4,5,6] 
produce [4,1],[5,2],[6,3].
Pista: La matriz resultante tiene c filas y f columnas: las dimensiones se intercambian. El elemento de la posición (i,j) termina en la posición (j, f-1-i)."""

#Crear matriz original
matrizMapa=[[1,2,3],
            [4,5,6]]


#Declarar filas y columnas
columnas= len(matrizMapa[0])
filas= len(matrizMapa)

#Crear matriz nueva
matriz = []

# Llenar la matriz
for i in range(columnas):
    fila_actual = []
    for j in range(filas):

        #Usar la formula y guardarla en un valor y luego en la fila
        valor = matrizMapa[filas-1-j][i]
        fila_actual.append(valor)

    #Agregar la fila doble a la matriz
    matriz.append(fila_actual)
    
print(matriz)