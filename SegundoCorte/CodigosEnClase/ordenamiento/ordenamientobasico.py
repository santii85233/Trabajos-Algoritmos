#comparar vecinos e intercambiar cuando estan alrevez y repetir hasta estar ordenado


#bubble sort
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
          while j>=0 and arr[j]> key:
               comparaciones+=1
               arr[j+1]= arr[j]
               j -=1
          arr[j+1]= key
          cambios+=1
     return arr,cambios,comparaciones

datos_bubble = [64, 25, 12, 22, 11, 90, 45, 33]
datos_selection = [64, 25, 12, 22, 11, 90, 45, 33]
datos_insertion = [64, 25, 12, 22, 11, 90, 45, 33]

arreglado, cambios, comparaciones = bubble_sort(datos_bubble)
print("El array ordenado con bubble sort es:", arreglado, ",realizando", cambios, "cambios y", comparaciones, "comparaciones.")

arreglado1, cambios1, comparaciones1 = selection_sort(datos_selection)
print("El array ordenado con selection sort es:", arreglado1, ",realizando", cambios1, "cambios y", comparaciones1, "comparaciones.")

arreglado2, cambios2, comparaciones2 = insertion_sort(datos_insertion)
print("El array ordenado con insertion sort es:", arreglado2, ",realizando", cambios2, "cambios y", comparaciones2, "comparaciones.")