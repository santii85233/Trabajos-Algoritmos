# Evalúa una expresión en notación postfija (como las calculadoras HP)
import math

def evaluar(expr):
    pila = []
    for tok in expr.split():
        if tok in "+-*/^r":
            b = pila.pop()          # ojo: primero sale el segundo operando
            a = pila.pop()
            if tok == "+": pila.append(a + b)
            elif tok == "r": pila.append(math.sqrt(a))
            elif tok == "-": pila.append(a - b)
            elif tok == "*": pila.append(a * b)
            elif tok == "^": pila.append(a ** b)
            else: pila.append(a / b)
        else:
            pila.append(float(tok))
    return pila.pop()

# (3 + 4) * 2        ->  3 4 + 2 *
# 10 - (6 / 3)       ->  10 6 3 / -
# (5 + 1) * (8 - 2)  ->  5 1 + 8 2 - *
for e in ["3 4 + 2 *", "10 6 3 / -", "5 1 + 8 2 - *"]:
    print(f"{e}  =  {evaluar(e):g}")

 #intentar incluir potencia y raiz cuadrada

for e in ["2 3 ^", "9 0.5 ^"]:
    print(f"{e}  =  {evaluar(e):g}")

for e in ["4 2 r", "9 2 r"]:
    print(f"{e}  =  {evaluar(e):g}")