import sympy as sp

def funcion(x):
    return sp.ln(x)

def interpolacion_lagrange(x_values, y_values):
    x = sp.Symbol('x')
    n = len(x_values)
    polinomio = 0
    
    for i in range(n):
        termino = 1
        for j in range(n):
            if j != i:
                termino *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polinomio += y_values[i] * termino
    
    return polinomio

def evaluar_polinomio(polinomio, valor):
    return polinomio.subs('x', valor)

modo = input("Selecciona el modo de entrada ('funcion' o 'valores'): ").strip().lower()
print('')

if modo == "funcion":
    cantidad_puntos = int(input("Ingrese la cantidad de puntos: "))
    x_values = []
    for i in range(cantidad_puntos):
        x = float(input(f"Ingrese el valor de x{i}: "))
        x_values.append(x)
    y_values = [funcion(x) for x in x_values]
elif modo == "valores":
    cantidad_puntos = int(input("Ingrese la cantidad de puntos: "))
    x_values = []
    y_values = []
    print('')
    for i in range(cantidad_puntos):
        x = float(input(f"Ingrese el valor de X{i}: "))
        x_values.append(x)
    print('')
    for i in range(cantidad_puntos):
        y = float(input(f"Ingrese el valor de y{i}: "))
        y_values.append(y)
else:
    print("Modo no válido.")
    exit()

polinomio = interpolacion_lagrange(x_values, y_values)

print("\nPolinomio de Lagrange:")
print(sp.simplify(polinomio))

evaluar = input("\n¿Desea evaluar el polinomio en un valor? (si/no): ")

if evaluar.lower() == "si":
    valor_evaluar = float(input("Ingrese el valor en el que desea evaluar el polinomio: "))
    resultado_evaluacion = evaluar_polinomio(polinomio, valor_evaluar)
    print("\nEl polinomio evaluado en x =", valor_evaluar, "es aproximadamente:", resultado_evaluacion)
elif evaluar.lower() == "no":
    print("\nNo se evaluó el polinomio.")
else:
    print("\nOpción no válida.")
