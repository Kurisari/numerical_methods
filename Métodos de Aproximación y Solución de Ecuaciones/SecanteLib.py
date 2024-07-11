import numpy as np
import scipy.optimize as optimize

# Definir la función a usar
def funcion(x):
    return x**3 - 2*x - 5

# Definir la función para el método de secante
def secante(func, x0, x1, tol, max_iter):
    root = optimize.newton(func, x0, fprime=None, args=(), tol=tol, maxiter=max_iter, fprime2=None, x1=x1, rtol=tol, full_output=False, disp=True)
    return root

# Solicitar al usuario las dos aproximaciones iniciales
x0 = float(input('Ingresa la primera aproximación inicial: '))
x1 = float(input('Ingresa la segunda aproximación inicial: '))
print()

tolerancia = 1e-6  # Define la tolerancia para el criterio de convergencia
max_iteraciones = 1000000  # Define el número máximo de iteraciones

# Aplicar el método de la secante
resultado = secante(funcion, x0, x1, tolerancia, max_iteraciones)

# Imprimir el resultado
print()
print("La raíz aproximada es:", resultado)
print()
