def sumaLista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[-1] + sumaLista(lista[:-1])

lista = [1, 2, 3, 4, 5]
resultado = sumaLista(lista)
print("La suma de la lista es:", resultado)