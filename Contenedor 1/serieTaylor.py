from math import *
import sympy as sp

def PolTaylor(a, n, x_val):
    x = sp.symbols('x')
    f = (x**3)*sp.log(x)
    F = f
    T = f.subs(x, a)
    
    for k in range(1, n+1):
        dfk = sp.diff(f, x)
        T = T + dfk.subs(x, a) * ((x - a) ** k) / sp.factorial(k)
        f = dfk
    
    print("Polinomio de Taylor:", T)
    
    T_numeric = T.evalf(subs={x: a})
    print("Valor numérico en el punto", a, ":", T_numeric)
    
    # Evaluar el polinomio de Taylor en el punto especificado
    T_evaluated = T.evalf(subs={x: x_val})
    print("Valor del polinomio en", x_val, ":", T_evaluated)

a = float(input('Digite alrededor de cual punto desea el polinomio: '))
n = int(input('Digite el orden del polinomio de Taylor: '))
x_val = float(input('Digite el valor en el que desea evaluar el polinomio: '))

PolTaylor(a, n, x_val)
