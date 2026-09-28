import random
import time

#Retos de Merge y Quick

comparaciones = 0
cambios = 0

#RETO 1

#Quicksort en el sitio con dos indices que se cruzan
def particion(arr, inicio, fin):
    global comparaciones, cambios
    pivote = arr[inicio]   #El pivote es el primer elemento
    i = inicio - 1   #i empieza a la izquierda
    j = fin + 1      #j empieza a la derecha
    while True:
        i += 1
        comparaciones += 1
        while arr[i] < pivote:   #i avanza mientras el elemento sea menor al pivote
            i += 1
            comparaciones += 1
        j -= 1
        comparaciones += 1
        while arr[j] > pivote:   #j retrocede mientras el elemento sea mayor al pivote
            j -= 1
            comparaciones += 1
        if i >= j:   #Si los indices se cruzan, se termina
            return j
        arr[i], arr[j] = arr[j], arr[i]
        cambios += 1

def quick_rec(arr, inicio, fin):
    if inicio < fin:
        p = particion(arr, inicio, fin)
        quick_rec(arr, inicio, p)   #Lado izquierdo
        quick_rec(arr, p + 1, fin)  #Lado derecho

def quick_sort(arr):
    global comparaciones, cambios
    comparaciones = 0
    cambios = 0
    quick_rec(arr, 0, len(arr) - 1)
    return arr, cambios, comparaciones

datos_quick = [64, 25, 12, 22, 11, 90, 45, 33]
arreglado, cambios1, comparaciones1 = quick_sort(datos_quick)
print("El array ordenado con quick sort es:", arreglado, ",realizando", cambios1, "cambios y", comparaciones1, "comparaciones.")


#RETO 2

#Se crea una lista de 500 numeros aleatorios
lista_aleatoria = []
for i in range(500):
    lista_aleatoria.append(random.randint(0, 9999))

#Se selecciona la misma lista pero ya ordenada (el peor caso para el primer elemento como pivote)
lista_ordenada = sorted(lista_aleatoria)

print("\nQuick sort con 500 datos")

inicio = time.perf_counter()
arreglado, cambios1, comparaciones1 = quick_sort(lista_aleatoria.copy())
final = time.perf_counter()
print("Lista aleatoria:", cambios1, "cambios,", comparaciones1, "comparaciones y", final - inicio, "segundos")

inicio = time.perf_counter()
arreglado, cambios2, comparaciones2 = quick_sort(lista_ordenada.copy())
final = time.perf_counter()
print("Lista ordenada:", cambios2, "cambios,", comparaciones2, "comparaciones y", final - inicio, "segundos")


"""
 *RETO 1: Quicksort en el sitio

 Se ordena sobre la misma lista, sin crear listas nuevas. Hay dos indices: i avanza desde
 la izquierda mientras arr[i] < pivote y j retrocede desde la derecha mientras arr[j] > pivote.
 Cuando los dos se detienen se intercambian y se sigue hasta que se cruzan (i >= j).
 El pivote es el primer elemento y la lista se parte en (inicio, j) y (j+1, fin).
 Con los 8 datos de clase: 6 cambios y 39 comparaciones.

 *RETO 2: caso que hace pesimo al Quicksort

 Con el primer elemento como pivote, una lista ya ordenada siempre deja el pivote en un
 extremo: una parte queda vacia y la otra con n-1 elementos, entonces se parte n veces
 en vez de log n veces. Con 500 datos (los mismos datos primero aleatorios y luego ordenados):

 Lista      | Comparaciones | Cambios
 Aleatoria  | unas 7000     | unos 1080
 Ordenada   | unas 125750   | menos de 15

 Como los datos son aleatorios los numeros de la lista aleatoria cambian un poco en cada
 ejecucion. Con la ordenada hace unas 18 veces mas comparaciones (casi n^2/2 = 125000)
 y tarda unas 10 veces mas (0.001 s contra 0.010 s).
"""
