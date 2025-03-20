import numpy as np
import sys

# Coeficientes de las ecuaciones
A = np.array([
    [-1, 1], # - X1 + X2 = 4
    [-2, 1], # -2X1 + X2 = 0
    [2, 3], # 2X1 + 3X2 = 5
    [1, 4] # X1 + 4X2 = 10
])

# Resultados de las ecuaciones
B = np.array([4, 0, 5, 10])

try:
    # Resolver el sistema de ecuaciones
    soluciones = np.linalg.lstsq(A, B, rcond=None)[0]

    print("Soluciones: ")
    print(f"X1 = {soluciones[0]:.2f}")
    print(f"X2 = {soluciones[1]:.2f}")

except np.linalg.LinAlgError as e:
    print("El sistema de ecuaciones no se puede resolver")
    print("Error: ", e)