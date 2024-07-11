from scipy.optimize import bisect
import numpy as np
import os

# Definir la función cuyas raíces se van a encontrar
def funcion(x):
    return x**3 - 2*x - 5

os.system('cls')

# Solicita al usuario los límites del intervalo [a, b]
a = float(input('Ingresa el valor del intervalo a: '))
b = float(input('Ingresa el valor del intervalo b: '))

# Llamada a la función bisect para encontrar la raíz de la función en el intervalo [a, b]
resultado = bisect(funcion, a, b)

# Imprimir el resultado
print()
print("La raíz aproximada es:", resultado)
print()