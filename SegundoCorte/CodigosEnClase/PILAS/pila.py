"""Pilas(stack): LIFO (Last In First Out)   
solo se accede al ultimo elemento agregado, el primero en salir es el ultimo en entrar
peek: ver el ultimo elemento sin eliminarlo
is_empty: verificar si la pila esta vacia
pop: eliminar el ultimo elemento agregado
push: agregar un elemento a la pila
size: devuelve el tamaño de la pila
top: devuelve el ultimo elemento agregado sin eliminarlo
"""
class Stack:
    def __init__(self):
        self.items = []
    def apilar(self, item):self.items.append(item)
    def desapilar(self):
        if self.vacia():return None
        return self.items.pop()
    def cima(self):return None if self.vacia() else self.items[-1]
    def vacia(self):
        return len(self.items) == 0    

#apilar sobre un array; apilo al final O(1) y desapilo al final O(1)
#Sobre una lista enlazada; apilo al inicio O(1) y desapilo al inicio O(1)

#(a[b]{c}) Y (a[b)c] "Está mal"
#Cada vez que se abre un paréntesis, corchete o llave, se apila. 
#Cada vez que se cierra, se desapila y se compara con el elemento desapilado.
#Si no son iguales, la expresión está mal. 
#Al final, si la pila está vacía, la expresión está bien.

def balanceados(s):
    p=Stack(); pares={')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in '([{': p.apilar(c)
        elif c in ')]}':
            if p.desapilar() != pares[c]: return False
    return True
    #return p.vacia() #si la pila está vacía, la expresión está bien

print("Comprobación eliminando la ultima línea de código")
print(balanceados("([]{})"))#return True
print(balanceados("([)]"))#return False
print(balanceados("((()"))#return False
print(balanceados("{}[]()"))#return True