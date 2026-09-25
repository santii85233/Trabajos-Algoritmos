def busqueda_binaria(lista, objetivo):
    izq, der = 0, len(lista) - 1  # n es len(lista)
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio  # Elemento encontrado
        elif lista[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
            
    return -1  # Elemento no encontrado

"""
1. ¿Que es n en la secuencia?

*n es la cantidad de elementos que hay dentro de la lista.

2.¿Cuántas veces se ejecuta el proceso si se duplican los datos?
*Se ejecutaria una vez más por el while ya que la busqueda binaria 
tiene una complejidad de logn y pues si se duplica se ejecutaria una vez más.

3. Dentro de esa secuencia se invoca otro proceso ¿cuántos procesos se invocan?

*Se invoca len() que es una función del python

4. que tipo de estructura de datos se utiliza

*Se utiliza una estructura de listas array.


Es la funcion de busqueda binaria y tiene una complejidad de 
O(logn)

"""