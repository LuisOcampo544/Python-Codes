import numpy as np
import sys

# Coeficientes de las ecuaciones
A = np.array([
    [1, -2, 3], # X1 - 2X2 + 3X3 = 9
    [-1, 3, -1], # - X1 + 3X2 -X3 = -6
    [2, -5, 5], # 2X1 - 5X2 + 5X3 = 17
    [1, 1, -3], # X1 + X2 - 3X3 = -1
    [1, 2, 0], # - X1 + 2X2 + 0X3 = 1
    [1, -1, 1] # X1 - X2 + X3 = 2
])

# Resultados de las ecuaciones
B = np.array([9, -6, 17, -1, 1, 2])

try:
    # Resolver el sistema de ecuaciones
    soluciones = np.linalg.lstsq(A, B, rcond=None)[0]

    print("Resultados: ")
    print(f"X1 = {soluciones[0]:.2f}")
    print(f"X2 = {soluciones[1]:.2f}")
    print(f"X3 = {soluciones[2]:.2f}")

except np.linalg.LinAlgError as e:
    print("El sistema de ecuaciones no se puede resolver")
    print("Error: ", e)