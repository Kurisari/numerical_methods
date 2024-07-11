import sympy as sp

def funcion(x):
    return sp.exp(x)+x**3+2*x**2+10*x-20

def biseccion(a, b, tolerancia, max_iteracion):
    x = sp.Symbol('x')
    f = funcion(x)
    
    if f.subs(x, a) * f.subs(x, b) >= 0:
        print("La función no cambia de signo en el intervalo dado.")
        return None
    
    iteracion = 0
    aux = None
    while (b - a) / 2.0 > tolerancia and iteracion < max_iteracion:
        c = (a + b) / 2.0
        error = abs((c - aux)/c)*100 if aux is not None else "N/A"
        print("Iteración", iteracion + 1, "- Aproximación:", c, "- Error:", error, "%")
        
        if f.subs(x, c) == 0:
            break
        
        if f.subs(x, c) * f.subs(x, a) < 0:
            b = c
        else:
            a = c
            
        iteracion += 1
        aux = c
        
    return c

a = float(input('Ingresa el valor del intervalo a: '))
b = float(input('Ingresa el valor del intervalo b: '))
print()

tolerancia = 1e-6
max_iteraciones = 1000000

resultado = biseccion(a, b, tolerancia, max_iteraciones)

if resultado is not None:
    print("La raíz aproximada es:", resultado)
else:
    print("El método de bisección no convergió.")
