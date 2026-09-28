import time

#Reto final: tabla de comparacion de todos los metodos de ordenamiento
#Se prueba el ejercicio ordenamiento2 imprimiendo la lista ordenada, las comparaciones, los intercambios y el tiempo

#Se selecciona la lista de clase
datos = [64, 25, 12, 22, 11, 90, 45, 33]

comparaciones = 0
cambios = 0

def bubble_sort(arr):
    cambios=0
    comparaciones=0
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            comparaciones+=1
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swapped= True
                cambios +=1
        if not swapped:
            break
    return arr, cambios ,comparaciones

def selection_sort(arr):
    cambios=0
    comparaciones=0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones+=1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        cambios+=1
    return arr,cambios,comparaciones

def insertion_sort(arr):
     cambios=0
     comparaciones=0
     for i in range(1,len(arr)):
          key = arr[i]
          j = i-1
          while j>=0:
               comparaciones+=1
               if arr[j]> key:
                    arr[j+1]= arr[j]
                    j -=1
               else:
                    break
          arr[j+1]= key
          cambios+=1
     return arr,cambios,comparaciones

#Merge Sort y Quicksort

#Mergesort es un algoritmo de ordenamiento
# que utiliza la técnica de divide y
# vencerás. Divide la lista en
# sublistas más pequeñas, las ordena y
# luego las combina para obtener la lista
# final ordenada.
#cambios: cada elemento que se escribe en arr al mezclar
def merge_sort(arr):
    global comparaciones, cambios
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            comparaciones += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            cambios += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            cambios += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            cambios += 1
    return arr

#Quicksort es un algoritmo de ordenamiento
# Elige un pivote y reorganiza el arreglo:
# los menores al pivote quedan a la izquierda
# y los mayores a la derecha.
# Luego repite lo mismo en cada lado.
#comparaciones: cada elemento se compara 3 veces contra el pivote (menor, igual y mayor)
#cambios: cada elemento que se coloca en una lista nueva
def quick_sort(arr):
    global comparaciones, cambios
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        comparaciones += 3 * len(arr)
        cambios += len(arr)
        return quick_sort(left) + middle + quick_sort(right)


# Heapsort y Bucket Sort

#Heapsort

def heapify(arr, n, i):
    global comparaciones, cambios
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        comparaciones += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        comparaciones += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        cambios += 1
        heapify(arr, n, largest)

#Con heapify solo no se ordena: se construye el heap y la raiz se manda al final
def heap_sort(arr):
    global comparaciones, cambios
    comparaciones = 0
    cambios = 0
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        cambios += 1
        heapify(arr, i, 0)
    return arr, cambios, comparaciones

#Bucket Sort
#Cada cubeta se ordena con insertion sort (en vez de sorted) para poder contar
def bucket_sort(arr):
    cambios = 0
    comparaciones = 0
    if len(arr) == 0:
        return arr, cambios, comparaciones

    min_value = min(arr)
    max_value = max(arr)
    bucket_range = (max_value - min_value) / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_value) / bucket_range)
        if index == len(arr):
            index -= 1
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0:
                comparaciones += 1
                if bucket[j] > key:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                else:
                    break
            bucket[j + 1] = key
            cambios += 1
        sorted_arr.extend(bucket)

    return sorted_arr, cambios, comparaciones


#Cada metodo trabaja con su propia copia de la lista y se mide el tiempo
tabla = []

def mostrar(nombre, arreglado, c, comp, tiempo):
    print("El array ordenado con", nombre, "es:", arreglado, ",realizando", c, "cambios y", comp, "comparaciones.")
    print("La funcion tardo:", tiempo, "segundos en completarse")
    tabla.append([nombre, comp, c, tiempo])

inicio = time.perf_counter()
arreglado, c, comp = bubble_sort(datos.copy())
final = time.perf_counter()
mostrar("bubble sort", arreglado, c, comp, final - inicio)

inicio = time.perf_counter()
arreglado, c, comp = selection_sort(datos.copy())
final = time.perf_counter()
mostrar("selection sort", arreglado, c, comp, final - inicio)

inicio = time.perf_counter()
arreglado, c, comp = insertion_sort(datos.copy())
final = time.perf_counter()
mostrar("insertion sort", arreglado, c, comp, final - inicio)

comparaciones = 0
cambios = 0
inicio = time.perf_counter()
arreglado = merge_sort(datos.copy())
final = time.perf_counter()
mostrar("merge sort", arreglado, cambios, comparaciones, final - inicio)

comparaciones = 0
cambios = 0
inicio = time.perf_counter()
arreglado = quick_sort(datos.copy())
final = time.perf_counter()
mostrar("quick sort", arreglado, cambios, comparaciones, final - inicio)

inicio = time.perf_counter()
arreglado, c, comp = heap_sort(datos.copy())
final = time.perf_counter()
mostrar("heap sort", arreglado, c, comp, final - inicio)

inicio = time.perf_counter()
arreglado, c, comp = bucket_sort(datos.copy())
final = time.perf_counter()
mostrar("bucket sort", arreglado, c, comp, final - inicio)

print("\nTabla de comparacion de los metodos de ordenamiento")
print("Metodo          | Comparaciones | Intercambios | Tiempo (s)")
for fila in tabla:
    print(fila[0], "|", fila[1], "|", fila[2], "|", f"{fila[3]:.8f}")


"""
 *TABLA DE COMPARACION DE TODOS LOS METODOS (8 datos de clase)

 Metodo          | Comparaciones | Intercambios | Tiempo (s)
 BubbleSort      | 25            | 14           | 0.00001414
 SelectionSort   | 28            | 8            | 0.00000800
 InsertionSort   | 18            | 7            | 0.00000523
 MergeSort       | 16            | 24           | 0.00001710
 QuickSort       | 78            | 26           | 0.00001350
 HeapSort        | 27            | 20           | 0.00001071
 BucketSort      | 2             | 2            | 0.00001296

 Todos imprimen la misma lista ordenada:
 [11, 12, 22, 25, 33, 45, 64, 90]

 Que se cuenta en cada uno (se dejo la logica de ordenamiento2, solo se agregaron los contadores):
 Bubble, Heap: cada swap. Selection: un swap por vuelta. Insertion: una insercion de la llave por vuelta.
 Merge: cada elemento que se escribe en la lista al mezclar.
 Quick: como crea listas nuevas y no hace swaps, cada elemento se compara 3 veces contra el pivote
 (menor, igual, mayor) y en cambios se cuenta cada elemento que se coloca en una lista nueva.
 Bucket: las inserciones dentro de las cubetas. Se cambio sorted(bucket) por insertion sort en cada
 cubeta porque sorted no permite contar. Usa n cubetas (8).
 Heap: ordenamiento2 solo tenia heapify, se agrego heap_sort (construir el heap y mandar la raiz al final).

 Selection en Python da 8 cambios y en C++ 7 porque el ciclo for llega hasta n en Python y hasta n-1 en C++.
 Los tiempos cambian en cada ejecucion y con solo 8 datos son muy pequeños, por eso
 se compara mejor con las comparaciones y los intercambios.
"""
