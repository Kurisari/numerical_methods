import math
import sympy as sym

x = sym.Symbol('x')
# fx = (2*x**3) - (4*sym.log(x))
# fx = 2**x
fx = x**2
x0 = 2.01
grado = 500
n = grado + 1

k = 0
polinomio = 0
while (k < n):
    derivada = fx.diff(x, k)
    derivadax0 = derivada.subs(x, x0)
    terminok = (derivadax0 / math.factorial(k)) * (x - x0)**k
    polinomio = polinomio + terminok
    k = k + 1

print(polinomio)
