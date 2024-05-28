import sympy as sp
from tabulate import tabulate

def funcion(x):
    return sp.ln(x)

def diferencias_divididas_newton(x_vals, y_vals=None, func=None):
    if func is not None:
        n = len(x_vals)
        F = [[None] * n for _ in range(n)]
        for i in range(n):
            F[i][0] = func(x_vals[i])
        for j in range(1, n):
            for i in range(n - j):
                F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_vals[i + j] - x_vals[i])
    elif y_vals is not None:
        n = len(x_vals)
        F = [[None] * n for _ in range(n)]
        for i in range(n):
            F[i][0] = y_vals[i]
        for j in range(1, n):
            for i in range(n - j):
                F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x_vals[i + j] - x_vals[i])
    else:
        raise ValueError("Debe proporcionar valores de 'y' o una función")
    return F

def imprimir_tabla_diferencias(F):
    headers = [f'Dif. Orden {i}' for i in range(len(F))]
    rows = []
    for j in range(len(F)):
        col = []
        for i in range(len(F[j])):
            if F[j][i] is not None:
                col.append(F[j][i])
            else:
                break
        rows.append(col)
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

def evaluar_newton(x, x_vals, F):
    n = len(x_vals)
    result = F[0][0]
    polinomio = F[0][0]
    for i in range(1, n):
        term = F[0][i]
        for j in range(i):
            term *= (x - x_vals[j])
        result += term
        polinomio += term
    return result, polinomio

modo = input("Selecciona el modo de entrada ('funcion' o 'valores'): ").strip().lower()
print()

if modo == 'funcion' or modo == 'valores':
    n = int(input('Ingresa el número de puntos de datos: '))
    print()
    if modo == 'funcion':
        x_vals = []
        for i in range(n):
            x = float(input(f'Ingresa el valor de x{i}: '))
            x_vals.append(x)
        F = diferencias_divididas_newton(x_vals, func=funcion)
    if modo == 'valores':
        x_vals = []
        y_vals = []
        for i in range(n):
            x = float(input(f'Ingresa el valor de x{i}: '))
            x_vals.append(x)
        print()
        for i in range(n):
            y = float(input(f'Ingresa el valor de y{i}: '))
            y_vals.append(y)
        F = diferencias_divididas_newton(x_vals, y_vals=y_vals)
    print("\nTabla de diferencias divididas:")
    imprimir_tabla_diferencias(F)
    resultado, polinomio = evaluar_newton(sp.Symbol('x'), x_vals, F)
    polinomio_simplificado = sp.simplify(polinomio)
    print("\nPolinomio interpolante de Newton:")
    print(polinomio_simplificado)
    evaluar = input("\n¿Quieres evaluar el polinomio interpolante? (si/no): ")
    if evaluar.lower() == 'si':
        x_eval = float(input('\nIngresa el valor de x donde quieres evaluar el polinomio interpolante: '))
        resultado_evaluado = resultado.subs(sp.Symbol('x'), x_eval)
        print(f'\nEl valor interpolado en x = {x_eval} es aproximadamente {resultado_evaluado}\n')
    elif evaluar.lower() == 'no':
        print("\nNo se evaluó el polinomio interpolante.\n")
    else:
        print("\nRespuesta no válida.\n")
else:
    print("Modo no válido. Debe ser 'funcion' o 'valores'\n")