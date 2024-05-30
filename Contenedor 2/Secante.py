import sympy as sp

def funcion(x):
    return sp.exp(x)+x**3+2*x**2+10*x-20

def secante(x0, x1, tol, max_iter):
    iteracion = 0
    aux = None
    
    while iteracion < max_iter:
        f_x1 = funcion(x1)
        f_x0 = funcion(x0)
        
        if abs(f_x1 - f_x0) < tol:
            print("Convergencia alcanzada en la iteración", iteracion + 1)
            return x1
        
        x_next = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        error = abs((x_next - aux)/x_next)*100 if aux is not None and x_next != 0 else "N/A"
        
        print("Iteración", iteracion + 1, "- Aproximación:", x_next, "Error:", error, "%")
        
        aux = x1
        x0 = x1
        x1 = x_next
        iteracion += 1
    
    print("El método de la secante no convergió después de", max_iter, "iteraciones.")
    return None

x0 = float(input('Ingresa la primera aproximación inicial: '))
x1 = float(input('Ingresa la segunda aproximación inicial: '))
print()

tolerancia = 1e-6
max_iteraciones = 1000

resultado = secante(x0, x1, tolerancia, max_iteraciones)

if resultado is not None:
    print("\nLa raíz aproximada es:", resultado)
else:
    print("\nEl método de la secante no convergió.")
