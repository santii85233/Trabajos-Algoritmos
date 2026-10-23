# ============================================================
#  Prueba corta · Segundo corte · EJERCICIO 3  (25 puntos)
#  Tema: pilas
#  Sistema: PrestaLab — historial de acciones del operador
#
#  NO MODIFIQUE el archivo pruebas_e3.py
#  Ejecute:   python3 pruebas_e3.py
# ============================================================


def historial_final(acciones):
    """Recibe una lista de cadenas. Cada cadena distinta de "DESHACER"
       se agrega al historial. La cadena "DESHACER" retira la ultima
       accion registrada; si el historial esta vacio, se IGNORA sin error.

       Devuelve el historial resultante como lista, de la accion mas
       antigua a la mas reciente.

       DEFECTO REPORTADO: el programa se cae cuando llega un "DESHACER"
       y el historial esta vacio."""
    pila = []
    for a in acciones:
        if a == "DESHACER":
            if pila:
                pila.pop()
            else:
                pass  # ignorar si la pila esta vacia
        else:
            pila.append(a)
    return pila


def profundidad_maxima(acciones):
    """Devuelve el mayor numero de acciones que el historial llego a
       tener en algun momento del recorrido.

       Ejemplo: ["a", "b", "DESHACER", "c"] -> 2
                (el historial llego a tener 2 elementos: a y b)"""
    pila = []
    max_profundidad = 0 # contador para la profundidad máxima alcanzada
    for a in acciones:
        if a == "DESHACER":
            if pila:
                pila.pop()
        else:
            pila.append(a)
            max_profundidad = max(max_profundidad, len(pila)) #Cuando agregamos una acción, actualizamos la profundidad máxima si es necesario
    return max_profundidad
    
