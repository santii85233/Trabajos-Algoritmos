#Retos de Ordenamientos Básicos: bubble, selection e insertion

#bubble sort SIN bandera (version vieja, solo para comparar con la nueva)
def bubble_sin_bandera(arr):
    cambios=0
    comparaciones=0
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            comparaciones+=1   #Se cuenta cada comparacion de vecinos
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                cambios +=1
    return arr, cambios ,comparaciones

#bubble sort CON bandera (Reto1)
def bubble_sort(arr):
    cambios=0
    comparaciones=0
    n=len(arr)
    for i in range(n):
        swapped=False   #La bandera empieza en False en cada pasada
        for j in range(0,n-i-1):
            comparaciones+=1
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swapped= True   #Hubo un intercambio
                cambios +=1
        if not swapped:   #Si no hubo ningun intercambio la lista ya esta ordenada
            break
    return arr, cambios ,comparaciones

def selection_sort(arr):
    cambios=0
    comparaciones=0
    n = len(arr)
    for i in range(n):
        min_idx = i   #Se supone que el menor es el de la posicion i
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
          key = arr[i]   #Se selecciona el elemento que se va a insertar
          j = i-1
          while j>=0:
               comparaciones+=1   #Aqui tambien se cuenta la comparacion que falla
               if arr[j]> key:
                    arr[j+1]= arr[j]
                    j -=1
               else:
                    break
          arr[j+1]= key
          cambios+=1
     return arr,cambios,comparaciones


#RETO 1
#Se selecciona la lista de clase, pero ya ordenada
datos_ordenados = [11, 12, 22, 25, 33, 45, 64, 90]
datos_bubble1 = datos_ordenados.copy()
datos_bubble2 = datos_ordenados.copy()
datos_insertion = datos_ordenados.copy()

arreglado, cambios, comparaciones = bubble_sin_bandera(datos_bubble1)
print("Bubble sin bandera:", cambios, "cambios y", comparaciones, "comparaciones.")

arreglado, cambios, comparaciones = bubble_sort(datos_bubble2)
print("Bubble con bandera:", cambios, "cambios y", comparaciones, "comparaciones.")

arreglado, cambios, comparaciones = insertion_sort(datos_insertion)
print("Insertion sort:", cambios, "cambios y", comparaciones, "comparaciones.")


#RETO 2
#Los registros del proyecto: (veces prestado, codigo del equipo)
#Se pone primero las veces prestado para que se ordene por ese dato
registros = [
    (14, "EQ-01"), (3, "EQ-02"),  (27, "EQ-03"), (9, "EQ-04"),  (21, "EQ-05"),
    (5, "EQ-06"),  (18, "EQ-07"), (30, "EQ-08"), (3, "EQ-09"),  (12, "EQ-10"),
    (25, "EQ-11"), (7, "EQ-12"),  (16, "EQ-13"), (22, "EQ-14"), (9, "EQ-15"),
    (29, "EQ-16"), (10, "EQ-17"), (19, "EQ-18"), (2, "EQ-19"),  (24, "EQ-20"),
]

#Se copia la lista para no perder los registros originales
registros_bubble = registros.copy()
arreglado, cambios, comparaciones = bubble_sort(registros_bubble)
print("\nRegistros ordenados por veces prestado:")
for veces, codigo in arreglado:
    print(codigo, "->", veces, "veces prestado")


#RETO 3
#Cada metodo trabaja con su propia copia de los registros
registros_bubble = registros.copy()
registros_selection = registros.copy()
registros_insertion = registros.copy()

arreglado, cambios_b, comparaciones_b = bubble_sort(registros_bubble)
arreglado, cambios_s, comparaciones_s = selection_sort(registros_selection)
arreglado, cambios_i, comparaciones_i = insertion_sort(registros_insertion)

print("\nMetodo          | Comparaciones | Intercambios |")
print("BubbleSort      |", comparaciones_b, "         |", cambios_b, "       |")
print("SelectionSort   |", comparaciones_s, "         |", cambios_s, "       |")
print("InsertionSort   |", comparaciones_i, "         |", cambios_i, "       |")


"""
 *RETO 1: bandera en Bubble

 Se agrego la variable swapped: empieza en False en cada pasada y si hubo un intercambio
 pasa a True. Si al terminar la pasada sigue en False la lista ya esta ordenada y se corta con break.
 Sobre los 8 datos ya ordenados:
   Bubble sin bandera: 28 comparaciones
   Bubble con bandera: 7 comparaciones (una sola pasada)
   Insertion sort: 7 comparaciones
 Baja de 28 a 7, igual que Insertion.
 (en insertion_sort se cuenta tambien la comparacion que falla y corta el while, si no
 se contara daria 0 en una lista ordenada)

 *RETO 2: registros por veces prestado

 Cada registro es una tupla (veces prestado, codigo). Se pone primero las veces prestado
 porque asi las tuplas se comparan por ese dato y los mismos metodos de ordenamiento sirven.
 Queda de menor a mayor. Para cambiar los datos solo se edita la lista registros.

 *RETO 3: tabla de comparaciones e intercambios con los 20 registros

 Metodo          | Comparaciones | Intercambios |
 BubbleSort      | 190           | 88           |
 SelectionSort   | 190           | 20           |
 InsertionSort   | 105           | 19           |

 Selection siempre hace las mismas comparaciones (n*(n-1)/2 = 190) sin importar el orden de los datos.
 Bubble es la que mas intercambios hace y Selection e Insertion son las que menos.
"""
