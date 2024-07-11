import numpy as np
import os

def krylov_method(A, v, k):
    n = len(A)
    V = np.zeros((n, k))
    V[:, 0] = v / np.linalg.norm(v)
    for i in range(1, k):
        V[:, i] = np.dot(A, V[:, i-1])
    return V

def format_characteristic_polynomial(coeffs):
    terms = []
    for i, coeff in enumerate(coeffs[::-1]):
        if coeff != 0:
            abs_coeff = np.round(abs(coeff), 10)
            if i == 0:
                term = f"{abs_coeff}"
            elif i == 1:
                term = f"{abs_coeff} λ"
            else:
                term = f"{abs_coeff} λ^{i}"
            if coeff < 0:
                terms.append(f"- {term}")
            else:
                terms.append(f"+ {term}")
    if not terms:
        return "0"
    polynomial_str = " ".join(terms[::-1])
    if polynomial_str.startswith("+ "):
        polynomial_str = polynomial_str[2:]
    return polynomial_str

def format_vector(vector):
    formatted_values = []
    for val in vector:
        if np.round(val.real, 10) != 0 or np.round(val.imag, 10) != 0:
            formatted_values.append(f"{np.round(val, 8).real:.8f}{' + ' if np.round(val.imag, 10) > 0 else ' - '}{abs(np.round(val, 8).imag):.8f}j" if np.round(val.imag, 10) != 0 else f"{np.round(val, 8).real:.8f}")
    formatted_vector = ", ".join(formatted_values)
    return f"[{formatted_vector}]"

def characteristic_polynomial(A, v, k):
    n = len(A)
    k = min(k, n)
    V = krylov_method(A, v, k)
    T = np.linalg.inv(V.T)
    poly_coeffs = np.poly(np.linalg.eigvals(A))
    polynomial_str = format_characteristic_polynomial(poly_coeffs)
    roots = np.roots(poly_coeffs)
    eigen_vectors = []
    for root in roots:
        eigen_val, eigen_vec = np.linalg.eig(A - root * np.eye(n))
        idx = np.argmin(np.abs(eigen_val - root))
        eigen_vectors.append(eigen_vec[:, idx])
    eigen_vectors = np.array(eigen_vectors).T
    return polynomial_str, roots, eigen_vectors

os.system('cls')

A = np.array([[5, -7, 7], 
              [4, -3, 4],
              [4, -1, 2]])

v = np.array([0, 0, 0])

k = 5

polynomial, roots, eigenvectors = characteristic_polynomial(A, v, k)
print("Polinomio característico:\n\n", polynomial, "\n")

print("Raíces del polinomio característico:\n")
for i, root in enumerate(roots):
    if np.iscomplex(root):
        print(f"λ{i+1} = {root}")
    elif np.real(root) == 0:
        print(f"λ{i+1} = {np.imag(root)}j")
    else:
        print(f"λ{i+1} = {np.real(root)}")

print("\nVectores propios:\n")
for i, vector in enumerate(eigenvectors.T):
    print(f"Vector {i+1}: {format_vector(vector)}")
print()
