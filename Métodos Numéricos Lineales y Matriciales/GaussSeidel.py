def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0[:]
    for k in range(max_iter):
        x_prev = x[:]
        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_) / A[i][i]
        if all(abs(x[i] - x_prev[i]) < tol for i in range(n)):
            return x
    raise ValueError("El método no converge después de %d iteraciones" % max_iter)

A = [[10, 3, 1],
     [5, -10, 3],
     [1, 3, 10]]

b = [14, -5, 14]

x0 = [0, 0, 0]

tol = 1e-20
max_iter = 1000000

sol = gauss_seidel(A, b, x0, tol, max_iter)

print("Solución encontrada: ", sol)
print('')
