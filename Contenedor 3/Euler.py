import numpy as np
from scipy.interpolate import PchipInterpolator
from tabulate import tabulate
import sympy as sp

def f(t, y):
    return t - y

y0 = 2
t0 = 0
t1 = 2
N = 10

h = (t1 - t0) / N

x = np.linspace(t0, t1, N)
y = np.zeros(N)

y[0] = y0

for i in range(1, N):
    y[i] = y[i-1] + h * f(x[i-1], y[i-1])

interp_func = PchipInterpolator(x, y)

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

print(f"\nEl polinomio interpolante evaluado en y0 ({y0}): {y0_value}")
print()