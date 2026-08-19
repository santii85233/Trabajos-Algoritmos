"""RETO 2  ·  La diagonal secreta   
Contexto: Un sistema sencillo de verificación usa las diagonales de una matriz cuadrada como código de control.
Se pide: Dada una matriz cuadrada, calcular la suma de la diagonal principal y la de la diagonal secundaria, y determinar si son iguales. Probar con {[1,2,3],[4,5,6],[7,8,9].
Pista: La diagonal principal son las posiciones donde fila e índice coinciden. Para la secundaria, cuando la fila avanza la columna retrocede: piensen en n-1-i."""

matrizCuadrada=[[1,2,3],
                [4,5,6],
                [6,8,9]]

suma1=0 #Se define la suma de las diagonales principales
suma2=0 #se define la suma de las diagonales secundarias

#Se empieza a iterar la matriz 
for i in range(len(matrizCuadrada)):

    #Se saca y suma el indice de la columna a sumar de la secundaria
    indice=len(matrizCuadrada)-1-i
    suma2+=matrizCuadrada[i][indice] 

    #Se iteran las filas junto a las columnas
    for j in range(len(matrizCuadrada)):
        #verifica que sea la principal
        if i==j:
            suma1+=matrizCuadrada[i][j] 

#Se da acceso o no si las diagonales coinciden o no
if suma1==suma2:
    print("Ambas diagonales coinciden, acceso permitido.")
else:
    print("Las diagonales no coinciden, acceso prohibido.")
