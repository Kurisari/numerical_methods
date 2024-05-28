import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    M = np.column_stack((A, b))
    for i in range(n):
        max_row = np.argmax(np.abs(M[i:, i])) + i
        M[[i, max_row]] = M[[max_row, i]]
        pivot = M[i, i]
        if np.abs(pivot) < 1e-100:
            raise ValueError("La matriz es singular")
        M[i] /= pivot
        for k in range(n):
            if k != i:
                factor = M[k, i]
                M[k] -= factor * M[i]
    solutions = M[:, -1]
    return solutions

A = [[4.0, 2.0, 5.0],
     [2.0, 5.0, 8.0],
     [5.0, 4.0, 3.0]]

b = [60.70, 92.90, 56.30]

try:
    soluciones = gauss_jordan(A, b)
    soluciones = [round(sol, 2) if isinstance(sol, float) else sol for sol in soluciones]
    print("Soluciones:", soluciones, "\n")
except ValueError as e:
    print(e)
