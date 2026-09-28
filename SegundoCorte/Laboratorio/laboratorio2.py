import random
import time

#Parte B Implementación de las busquedas binaria y secuencial

def binaria(v, x):
    comps = 0
    izq, der = 0, len(v) - 1
    while izq <= der:
        medio = (izq + der) // 2
        comps += 1
        if v[medio][0] == x:
            return medio, comps
        elif v[medio][0] < x:
            izq = medio + 1
        else:
            der = medio - 1
    return -1, comps


def secuencial(v, x):
    comps = 0
    for i in range(len(v)):
        comps += 1
        if v[i][0] == x:
            return i, comps
    return -1, comps

#Parte C Implementación de los basic sorts con contadores de cambios y comparaciones 

def bubble_sort(arr):
    cambios = 0
    comparaciones = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                cambios += 1
        if not swapped:
            break
    return arr, cambios, comparaciones

def selection_sort(arr):
    cambios = 0
    comparaciones = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        cambios += 1
    return arr, cambios, comparaciones

def insertion_sort(arr):
    cambios = 0
    comparaciones = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
        cambios += 1
    return arr, cambios, comparaciones

#Parte D Implementación del quicksort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

pruebas = [
    (1014638621, "Ana"), (100373462754, "Luis"), (1027463725, "Marta"), (100932176563, "Pedro"), (1021837261873, "Sofia"),
    (1005387126, "Juan"), (10183721665, "Laura"), (103035427168, "Carlos"), (10138726318, "Diana")
]

def crear_datos():
    n = int(input("Cuantos registros de Usuario desea implementar: "))
    datos = []
    for i in range(n):
        codigo = input(f"Registro {i+1} - Nombre Usuario: ").strip()
        veces = int(input(f"Registro {i+1} - Documento Usuario: "))
        datos.append((veces, codigo))
    return datos


def aleatorios(n):
    return [(random.randint(0, 99999), f"U{i}") for i in range(n)]


#Parte B: tabla comparativa (primero, medio, ultimo, no existe)
def parte_b(datos):
    v, _, _ = insertion_sort(datos.copy())   #la binaria los datos ordenados, el _ es para ignorar los datos del return
    casos = [("Primero", v[0][0]), ("Del medio", v[len(v) // 2][0]),
             ("Ultimo", v[-1][0]), ("No existe", -1)]
    print(f"\nPARTE B - {len(v)} registros ordenados por documento")
    print(f"{'Caso':<11}| {'Clave':<7}| {'Secuencial':<11}| {'Binaria'}")
    for nombre, x in casos:
        _, cs = secuencial(v, x)
        _, cb = binaria(v, x)
        print(f"{nombre:<11}| {x:<7}| {cs:<11}| {cb}")
 
#Parte C: basicos con datos desordenados y ya ordenados
def parte_c(datos):
    pass
#Parte D: tiempo de Bubble contra Quicksort con tres tamaños
def parte_d():
    pass
 
def Menu():
    print("============LABORATORIO===========")
    print("= Ingrese el numero para:        =")
    print("= 1.Realizar coleccion de datos  =")
    print("= 0.Salir                        =")
    print("==================================")
 
def submenu(datos):
    while True:
        print("\n1. Parte B (busquedas)  2. Parte C (basicos)  3. Parte D (tiempos)  0. Volver")
        opcion = int(input("Ingrese la opción:"))
        if opcion == 1:
            parte_b(datos)
        elif opcion == 2:
            parte_c(datos)
        elif opcion == 3:
            parte_d()
        elif opcion == 0:
            break
        else:
            print("Ingrese una opcion válida.")
 
while True:
    Menu()
    opcion = int(input("Ingrese la opción:"))
    if opcion == 1:
        submenu(crear_datos())
    elif opcion==2:
        submenu(pruebas)
    elif opcion == 0:
        break
    else:
        print("Ingrese una opcion válida.")
 