import numpy as np

def print_matrix(A, b):
    """Imprimir la matriz aumentada"""
    augmented_matrix = np.hstack([A, b.reshape(-1, 1)])
    print("Matriz aumentada:") 
    print(augmented_matrix)
    print()

def solve_and_print(S, vec, vec_name):
    print(f"Resolviendo para el vector {vec_name}:")
    print(f"Vector a comprobar: {vec}")
    
    # Crear la matriz aumentada
    A = S.T
    b = vec
    
    print_matrix(A, b) 
    
    try:
        # Resolver el sistema de ecuaciones lineales Sx = vec
        coeffs = np.linalg.lstsq(A, b, rcond=None)[0]
        if np.allclose(A @ coeffs, b):
            print(f"El vector {vec_name} puede ser expresado como una combinación lineal de los vectores en S con los coeficientes: {coeffs}")
        else:
            print(f"El vector {vec_name} no puede ser expresado como una combinación lineal de los vectores en S.")
    except np.linalg.LinAlgError:
        print(f"El vector {vec_name} no puede ser expresado como una combinación lineal de los vectores en S.")
    print("-" * 50)

# Definir los vectores en el conjunto S
S = np.array([
    [6, -7, 8, 6],
    [4, 6, -4, 1]
])

# Definir los vectores u, v, w, z
u = np.array([-42, 113, -112, -60])
v = np.array([49/2, 98/4, -14, 19/2])
w = np.array([-4, -14, 27/2, 53/8])
z = np.array([8, 4, -1, 17/4])

# Lista de vectores a comprobar
vectors = [u, v, w, z]
vector_names = ['u', 'v', 'w', 'z']

# Verificar si cada vector puede ser expresado como una combinación lineal de los vectores en S
for i, vec in enumerate(vectors):
    solve_and_print(S, vec, vector_names[i])
