import random
import time

#Retos de Heap y Bucket

comparaciones = 0
cambios = 0

#RETO 1

#Heapsort de maximos: la raiz es el mayor
def heapify_max(arr, n, i):
    global comparaciones, cambios
    mayor = i   #Se supone que el mayor es el padre
    izq = 2 * i + 1
    der = 2 * i + 2
    if izq < n:
        comparaciones += 1
        if arr[izq] > arr[mayor]:
            mayor = izq
    if der < n:
        comparaciones += 1
        if arr[der] > arr[mayor]:
            mayor = der
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        cambios += 1
        heapify_max(arr, n, mayor)

def heap_sort_max(arr):
    global comparaciones, cambios
    comparaciones = 0
    cambios = 0
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):   #Se construye el heap
        heapify_max(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]   #La raiz se manda al final
        cambios += 1
        heapify_max(arr, i, 0)
    return arr, cambios, comparaciones

#Heapsort de minimos: la raiz es el menor (se cambian los > por <)
def heapify_min(arr, n, i):
    global comparaciones, cambios
    menor = i   #Se supone que el menor es el padre
    izq = 2 * i + 1
    der = 2 * i + 2
    if izq < n:
        comparaciones += 1
        if arr[izq] < arr[menor]:
            menor = izq
    if der < n:
        comparaciones += 1
        if arr[der] < arr[menor]:
            menor = der
    if menor != i:
        arr[i], arr[menor] = arr[menor], arr[i]
        cambios += 1
        heapify_min(arr, n, menor)

def heap_sort_min(arr):
    global comparaciones, cambios
    comparaciones = 0
    cambios = 0
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_min(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        cambios += 1
        heapify_min(arr, i, 0)
    return arr, cambios, comparaciones

datos_max = [64, 25, 12, 22, 11, 90, 45, 33]
datos_min = [64, 25, 12, 22, 11, 90, 45, 33]

arreglado, cambios1, comparaciones1 = heap_sort_max(datos_max)
print("El array ordenado con heap sort de maximos es:", arreglado, ",realizando", cambios1, "cambios y", comparaciones1, "comparaciones.")

arreglado, cambios2, comparaciones2 = heap_sort_min(datos_min)
print("El array ordenado con heap sort de minimos es:", arreglado, ",realizando", cambios2, "cambios y", comparaciones2, "comparaciones.")


#RETO 2

#Bucket sort con k cubetas, cada cubeta se ordena con insertion sort
def bucket_sort(arr, k):
    cambios=0
    comparaciones=0
    maximo = max(arr)
    cubetas = []
    for i in range(k):   #se crean las cubetas vacias
        cubetas.append([])
    for numero in arr:
        posicion = numero * k // (maximo + 1)   #se selecciona la cubeta que le toca al numero
        cubetas[posicion].append(numero)
    resultado = []
    for cubeta in cubetas:
        for i in range(1, len(cubeta)):   #Insertion sort dentro de la cubeta
            key = cubeta[i]
            j = i - 1
            while j >= 0:
                comparaciones += 1
                if cubeta[j] > key:
                    cubeta[j + 1] = cubeta[j]
                    j -= 1
                else:
                    break
            cubeta[j + 1] = key
            cambios += 1
        resultado = resultado + cubeta
    return resultado, cambios, comparaciones

#Se crea una lista de 1000 numeros aleatorios

datos_bucket = []
for i in range(1000):
    datos_bucket.append(random.randint(0, 9999))

print("\nBucket sort con 1000 datos")

inicio = time.perf_counter()
arreglado, cambios1, comparaciones1 = bucket_sort(datos_bucket.copy(), 5)
final = time.perf_counter()
print("5 cubetas:", cambios1, "cambios,", comparaciones1, "comparaciones y", final - inicio, "segundos")

inicio = time.perf_counter()
arreglado, cambios2, comparaciones2 = bucket_sort(datos_bucket.copy(), 50)
final = time.perf_counter()
print("50 cubetas:", cambios2, "cambios,", comparaciones2, "comparaciones y", final - inicio, "segundos")


"""
 *RETO 1: Heapsort de minimos, ¿que cambio?

 1. En heapify se cambian los > por < y la variable mayor pasa a ser menor: el padre
    tiene que ser menor que sus hijos, asi la raiz del heap es el minimo.
 2. Como el algoritmo manda la raiz al final de la lista en cada vuelta, ahora se van
    al final los menores y la lista queda ordenada de MAYOR a MENOR:
    [90, 64, 45, 33, 25, 22, 12, 11]. Para dejarla de menor a mayor habria que
    invertirla al final o usar otra lista.
 3. Lo demas es igual: construir el heap, intercambiar la raiz con el ultimo y volver a arreglar.
    Con los 8 datos: maximos 20 cambios y 27 comparaciones, minimos 20 cambios y 28 comparaciones.

 *RETO 2: Bucket Sort con 5 y con 50 cubetas (1000 datos, los mismos en las dos pruebas)

 Cubetas | Comparaciones | Cambios
 5       | unas 51000    | 995
 50      | unas 5700     | 950

 Como los datos son aleatorios los numeros cambian un poco en cada ejecucion.
 Con 5 cubetas cada una queda con unos 200 datos y el insertion sort de cada cubeta hace
 muchas comparaciones. Con 50 quedan unos 20 por cubeta y las comparaciones bajan casi 9 veces
 (el tiempo pasa de unos 0.003 s a unos 0.0005 s).
 Mas cubetas no es gratis (hay que crearlas y recorrerlas aunque queden vacias), por eso
 hay un punto donde dejan de ayudar.
"""
