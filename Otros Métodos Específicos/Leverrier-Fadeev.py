import numpy as np

def leverrier_faddeev_poly(A):
    n = A.shape[0]
    B = np.eye(n)
    C = np.zeros_like(A)
    coeffs = [1]
    for k in range(1, n+1):
        C = np.dot(A, C) + (k - 1) * B
        B = np.dot(A, B)
        alpha = -np.trace(B) / k
        B += alpha * np.eye(n)
        coeffs.append(alpha)
    return np.poly1d(coeffs) 

def format_characteristic_polynomial(coeffs):
    terms = []
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        exp = degree - i
        abs_coeff = np.round(abs(coeff), 10)
        if exp == 0:
            term = f"{abs_coeff}"
        elif exp == 1:
            term = f"{abs_coeff} λ"
        else:
            term = f"{abs_coeff} λ^{exp}"
        if coeff < 0:
            terms.append(f"- {term}")
        else:
            terms.append(f"+ {term}")
    if not terms:
        return "0"
    polynomial_str = " ".join(terms)
    if polynomial_str.startswith("+ "):
        polynomial_str = polynomial_str[2:]
    return polynomial_str

def format_root(i, root):
    real_part = np.round(root.real, 10)
    imag_part = np.round(root.imag, 10)
    if real_part == 0 and imag_part == 0:
        return f"λ{i+1} = 0"
    elif real_part == 0:
        return f"λ{i+1} = {imag_part}j"
    elif imag_part == 0:
        return f"λ{i+1} = {real_part}"
    else:
        sign = "+" if imag_part > 0 else "-"
        return f"λ{i+1} = {real_part} {sign} {abs(imag_part)}j"

def format_eigenvector(i, eigenvector):
    formatted_values = []
    for val in eigenvector:
        if np.round(val.real, 10) != 0 or np.round(val.imag, 10) != 0:
            formatted_values.append(f"{np.round(val, 8).real:.8f}{' + ' if np.round(val.imag, 10) > 0 else ' - '}{abs(np.round(val, 8).imag):.8f}j" if np.round(val.imag, 10) != 0 else f"{np.round(val, 8).real:.8f}")
    formatted_vector = ", ".join(formatted_values)
    return f"Vector {i+1}: [{formatted_vector}]"

A = np.array([[5, -7, 7], 
              [4, -3, 4],
              [4, -1, 2]])

pol = leverrier_faddeev_poly(A)
formatted_polynomial = format_characteristic_polynomial(pol.coefficients)
print("Polinomio característico:\n")
print(formatted_polynomial, "\n")

eigenvalues, eigenvectors = np.linalg.eig(A)

formatted_roots = [format_root(i, root) for i, root in enumerate(eigenvalues)]
print("Raíces del polinomio característico:\n")
for root in formatted_roots:
    print(root)

formatted_eigenvectors = [format_eigenvector(i, eigenvector) for i, eigenvector in enumerate(eigenvectors.T)]
print("\nVectores propios:\n")
for vector in formatted_eigenvectors:
    print(vector)
print()
