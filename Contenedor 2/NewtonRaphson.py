import sympy as sp

def funcion(x):
    return -x**2 + 2*x + 1

def newton_raphson(funcion, x0, tol, max_iter):
    x = sp.Symbol('x')
    f = funcion(x)
    f_derivada = sp.diff(f, x)
    aux = None
    iteracion = 0
    while iteracion < max_iter:
        f_eval = f.subs(x, x0) 
        f_derivada_eval = f_derivada.subs(x, x0)
        error = abs((x0 - aux)/x0)*100 if aux is not None else "N/A"
        print("Iteración", iteracion + 1, "- Aproximación:", x0, "- Error:", error, "%")
        if abs(f_eval) < tol:
            print()
            print("La solución convergió en la iteración", iteracion + 1)
            return x0
        if f_derivada_eval == 0:
            print()
            print("La derivada se anula en la iteración", iteracion + 1)
            return None
        aux = x0
        x0 = x0 - f_eval / f_derivada_eval
        iteracion += 1
    print()
    print("El método de Newton-Raphson no convergió en", max_iter, "iteraciones.")
    return None

x0 = float(input('Ingresa la aproximación inicial: '))
print()

tolerancia = 1e-6
max_iteraciones = 1000000

resultado = newton_raphson(funcion, x0, tolerancia, max_iteraciones)

if resultado is not None:
    print("La raíz aproximada es:", resultado)
else:
    print("El método de Newton-Raphson no convergió.")