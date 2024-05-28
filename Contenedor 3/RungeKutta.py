import numpy as np
from tabulate import tabulate
import sympy as sp

def f(t, y):
    return y - t**2 + 1

def runge_kutta_4th_order(f, t0, y0, t_final, h):
    N = int((t_final - t0) / h) + 1
    t = np.linspace(t0, t_final, N)
    y = np.zeros(N)
    y[0] = y0
    for i in range(1, N):
        k1 = h * f(t[i-1], y[i-1])
        k2 = h * f(t[i-1] + h/2, y[i-1] + k1/2)
        k3 = h * f(t[i-1] + h/2, y[i-1] + k2/2)
        k4 = h * f(t[i-1] + h, y[i-1] + k3)
        
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return t, y

y0 = 0.5  # Condición inicial
t0 = 0    # Punto inicial en el eje x
t1 = 2    # Punto final en el eje x
N = 10   # Número de puntos (incluyendo x0 y x1)

h = (t1 - t0) / N

x, y = runge_kutta_4th_order(f, t0, y0, t1, h)

table = []
for i, xi in enumerate(x):
    table.append([f"{xi:.2f}", f"{y[i]:.6f}"])

print("Los puntos de red son:\n")

headers = ["Valores de t", "Valores de y"]
print(tabulate(table, headers, tablefmt="fancy_grid"))

t = sp.symbols('t')
polynomial = 0

for i in range(len(x)):
    term = y[i]
    for j in range(len(x)):
        if i != j:
            term *= (t - x[j]) / (x[i] - x[j])
    polynomial += term

simplified_polynomial = sp.simplify(polynomial)

print("\nPolinomio interpolante simplificado:\n")
print(simplified_polynomial)

y0_value = simplified_polynomial.subs(t, y0)

print(f"\nEl polinomio interpolante evaluado en y0 ({t0}): {y0_value}")
print()