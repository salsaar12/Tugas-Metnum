import numpy as np
import scipy.linalg

def solve_crout(A, b):
    P, L, U = scipy.linalg.lu(A, permute_l=True)
    y = np.linalg.solve(L, np.dot(P, b))
    x = np.linalg.solve(U, y)
    return x

# Contoh penggunaan:
A = np.array([[2, 1], [1, -1]])
b = np.array([7, 1])
x = solve_crout(A, b)
print("Solusi menggunakan metode dekomposisi Crout:", x)
