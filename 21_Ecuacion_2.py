import numpy as np
import sys

# Coeficientes de las ecuaciones
A = np.array([
    [-2, -3], # - 2X1 -3X2 = -4
    [6, 1], # 6X1 + X2 = -36
    [-4, 9], # - 4X1 + 9X2 = -13
    [1, -3] # X1 - 3X2 = 12
])

# Resultados de las ecuaciones
B = np.array([-4, -36, -13, 12])

try:
    # Resolver el sistema de ecuaciones
    soluciones = np.linalg.lstsq(A, B, rcond=None)[0]

    print("Resultados: ")
    print(f"X1 = {soluciones[0]:.2f}")
    print(f"X2 = {soluciones[1]:.2f}")

except np.linalg.LinAlgError as e:
    print("El sistema de ecuaciones no se puede resolver")
    print("Error: ", e)