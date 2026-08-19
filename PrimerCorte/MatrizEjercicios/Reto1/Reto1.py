"""  RETO 1  ·  El mapa de calor de la sala de estudio   
Contexto: La Sala Knuth registra cuántas personas hay en cada franja horaria (6 franjas) de lunes a viernes (5 días). La coordinación quiere reorganizar los horarios de monitoría.
Se pide: Construir la matriz y responder tres cosas: cuál fue la franja más congestionada de toda la semana (con su día y hora), qué día tuvo mayor ocupación total, y 
cuáles franjas estuvieron siempre por debajo de 5 personas.
Pista: Para la franja más congestionada necesitan guardar no solo el máximo, sino también en qué fila y columna lo encontraron."""
#Definir matriz con filas como franjas y columnas como personas que asistieron
matrizMonitorias=[[2,4,6,12,4], #"08:00 am- 10:00 am"
                  [1,5,2,11,2], #10:00 am- 12:00 pm
                  [3,4,5,7,1],  #12:00 pm- 1:00 pm
                  [0,2,0,0,0],  #3:00 pm- 4:00 pm
                  [0,4,6,9,5],  #4:00 pm- 5:00 pm
                  [2,4,6,9,5]]  #5:00 pm- 6:00 pm

#Definir que dia significa cada columna
semana=["Lunes","Martes","Miercoles","Jueves","Viernes"]

#Definir que franja representa cada fila
franjash=["08:00 am- 10:00 am","10:00 am- 12:00 pm","12:00 pm- 1:00 pm","3:00 pm- 4:00 pm","4:00 pm- 5:00 pm","5:00 pm- 6:00 pm"]

dias=5 #dias de la semana
franjas=6 # total de franjas
totalesFranja=[] #Lista para guardar la suma total de personas por franja
totalesDia =[] #Lista para guardar la suma total de personas por dia
totalDia =0 #Entero para guardar la cantidad total de personas por dia
totalFranja=0 #Entero para guardar la cantidad de personas por franja
maximo=0 # maximo de personas por franja y por dia 

#Ciclo para recorrer la matriz
for i in range(len(matrizMonitorias)):
    for j in range(len(matrizMonitorias[dias])):

        #Analiza si esa posición es el maximo de personas en una franja
        if matrizMonitorias[i][j] >maximo:
            maximo= matrizMonitorias[i][j]
            dia= j
            hora= i

        #Hace la suma de personas por franja
        totalFranja+=matrizMonitorias[i][j]
    totalesFranja.append(totalFranja)
    totalFranja=0

#Hace la suma de cada columna de cada fila es decir el recuento de personas por dia
for c in range(dias):
        for f in range(franjas):

        #Se hace el recuento del total de personas por dia
            totalDia +=matrizMonitorias[f][c]

    #Se agregan a una lista y se reinicia para el siguiente dia
        totalesDia.append(totalDia)
        totalDia=0 

print("El dia con más asistentes fue el ", semana[dia],"En la franja", franjash[hora], "con un total de ", maximo, "personas")

#Se reinicia para ser usada para analizar el maximo de personas por dia 
maximo=0

#Se recorre la lista de la suma de los dias y se encuentra al mayor y se almacena
for x in range(len(totalesDia)):
    if totalesDia[x] >maximo:
        maximo=totalesDia[x]
        indice=x

#Se imprime 
print("El dia con más personas en total, fue el",semana[indice],", contando con un total de",maximo,"Personas.")
maximo = 0 

#Se halla las franjas con menos de 5 personas
for x in range(len(totalesFranja)):
    if totalesFranja[x] <5:
        maximo=totalesFranja[x]
        indice=x
        print("La franja",franjash[x],"se encuentra por debajo de 5 personas de asistencia, contando con ",maximo,"personas.")
