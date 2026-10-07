""" Busquedas por codigo 
O(n)recorrer la lista(N registros y n comparaciones)
O (log n) ordenar la lista y busqueda(por cada registro se organiza)
O(1)Hash (conjuntos/mapas)

Conjunto:
    Guarda elementos unicos, no permite duplicados, no tiene orden, es mutable
    sin repeticion y sin orden.(¿Este elemento ya existe?)
Mapa:(diccionario)
    Guarda elementos en pares clave-valor, no permite claves duplicadas, es mutable
    sin repeticion y sin orden.(¿Que valor tiene esta clave?)

Funcion hash:
    Recibe un elemento y devuelve un numero entero
        -Es deterministico: el mismo elemento siempre devuelve el mismo numero
        -rapida: Si calcula es mas costoso que recorrer.
        -Bien distribuida: Los elementos se distribuyen uniformemente en el rango de numeros enteros.

"""
a={"papel","lapiz","cuaderno"}
b={"vidrio","madera","plastico"}

print(a.union(b)) #union
print(a.intersection(b)) #interseccion
print(a.difference(b)) #diferencia

print(a | b) #union
print(a & b) #interseccion
print(a - b) #diferencia

mapa={"REC-00042": 42}
print(mapa["REC-00042"])

set1=set()
dict1=dict()

def hash(self,clave):
    h=0
    for c in str(clave):
        h= (h*31 + ord(c)) % 100
    return h

#ANA NAA

"""
1. funcion hash para los nomnbres de los alumnos 

colisiones:cuando dos elementos tienen el mismo valor hash,
           se guarda en una lista enlazada, se busca en la lista enlazada.
           -consume mas cache

direccionamiento abierto: cuando dos elementos tienen el mismo valor hash,
           se busca la siguiente cubeta vacia para guardar el elemento,
           todo esto se aloja en un arreglo de cubetas,
           para cada cubeta puede guardar un elemento o una lista enlazada de elementos.
           -Al eliminar rompe las cadenas creadas

Factor de carga: cantidad de elementos / cantidad de cubetas

lambda, factorCarga = n(elementos)/m(cubetas)
lambda=0.5, no hay muchas colisiones, lambda>0.5 se presentan colisiones

lambda = 5 cada busqueda recorre 5 claves.
    si lambda es mayor a 0.75, se recomienda redimensionar el arreglo de cubetas, 
    para reducir el factor de carga y mejorar el rendimiento (rehash).
"""