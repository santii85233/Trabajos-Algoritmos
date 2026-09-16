def invertir(cadena):
    if len(cadena)==0: #Caso Base cadena vacia
        return ""
    else:
        return cadena[-1] + invertir(cadena[:-1]) #devuelve el ultimo elemento de la cadena y la inversion recursiva del resto
print(invertir("Hola Mundo"))