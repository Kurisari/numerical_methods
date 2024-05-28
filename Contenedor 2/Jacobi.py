def jacobi(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0[:]
    for k in range(max_iter):
        x_prev = x[:]
        for i in range(n):
            sum_ = sum(A[i][j] * x_prev[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_) / A[i][i]
        if all(abs(x[i] - x_prev[i]) < tol for i in range(n)):
            return x
    raise ValueError("El método no converge después de %d iteraciones" % max_iter)

A = [[10, 2, 1],
     [1, 5, 1],
     [2, 3, 10]]

b = [7, -8, 6]

x0 = [0, 0, 0]

tol = 1e-20
max_iter = 1000000

sol = jacobi(A, b, x0, tol, max_iter)

print("Solución encontrada:", sol)
print('')
