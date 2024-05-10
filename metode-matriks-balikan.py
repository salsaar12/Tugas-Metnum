import numpy as np

def solve_matrix_inverse(A, b):
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, b)
    return x

# Testing code
A = np.array([[2, 1], [1, -1]])
b = np.array([7, 1])
x = solve_matrix_inverse(A, b)
print("Solusi menggunakan metode matriks balikan:", x)
