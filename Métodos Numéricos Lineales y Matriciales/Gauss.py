import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    M = np.column_stack((np.array(A, dtype=float), np.array(b, dtype=float)))
    for i in range(n):
        pivot = M[i, i]
        if np.abs(pivot) < 1e-100:
            raise ValueError("La matriz es singular")
        for k in range(i+1, n):
            factor = M[k, i] / pivot
            M[k, i:] -= factor * M[i, i:]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:])) / M[i, i]
    
    return x

A = [
    [1, 2, -3],
    [1, 0, 5],
    [0, 0, 0]
]

b = [1, 0, 0]

try:
    soluciones = gauss_elimination(A, b)
    soluciones = [round(sol, 5) if isinstance(sol, float) else sol for sol in soluciones]
    print("Soluciones:", soluciones, "\n")
except ValueError as e:
    print(e)

