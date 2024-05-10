import numpy as np
import scipy.linalg

def solve_lu_gauss(A, b):
    P, L, U = scipy.linalg.lu(A)
    y = np.linalg.solve(L, np.dot(P, b))
    x = np.linalg.solve(U, y)
    return x

# Testing code
A = np.array([[2, 1], [1, -1]])
b = np.array([7, 1])
x = solve_lu_gauss(A, b)
print("Solusi menggunakan metode dekomposisi LU Gauss:", x)
