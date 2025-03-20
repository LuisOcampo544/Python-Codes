# Elaborado por Luis Carlos Ocampo Rivera
import numpy as np

def calcular_determinante(matriz):
    return round(np.linalg.det(matriz), 0)

def calcular_inversa(matriz):
    return np.linalg.inv(matriz)

def calcular_suma(matriz1, matriz2):
    return matriz1 + matriz2

def calcular_resta(matriz1, matriz2):
    return matriz1 - matriz2

def calcular_multiplicacion(matriz1, matriz2):
    return matriz1 @ matriz2

def pedir_datos(tamaño):
    matriz = []
    for i in range(tamaño):
        fila = list(map(int, input(f"Ingrese los elementos de la fila {i+1}: ").split()))
        matriz.append(fila)
    return np.array(matriz)

def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()

def main():
    tamaño = int(input("Ingrese el número de filas y columnas de la matriz: "))
    matriz1 = pedir_datos(tamaño)
    matriz2 = pedir_datos(tamaño)
    operacion = input("Ingrese el tipo de operación (1.-Suma, 2.-Resta, 3.-Multiplicación): ")

    if operacion == "1":
        matriz_resultante = calcular_suma(matriz1, matriz2)
    elif operacion == "2":
        matriz_resultante = calcular_resta(matriz1, matriz2)
    elif operacion == "3":
        matriz_resultante = calcular_multiplicacion(matriz1, matriz2)
    else:
        print("Operación no válida")
        return

    print("\nMatriz resultante:")
    mostrar_matriz(matriz_resultante)

    print(f"Determinante de la matriz 1: {calcular_determinante(matriz1)}")
    print(f"Determinante de la matriz 2: {calcular_determinante(matriz2)}")
    print(f"Determinante de la matriz resultante: {calcular_determinante(matriz_resultante)}")

    print("\nInversa de la matriz 1: ")
    print(f"{calcular_inversa(matriz1)}")
    print("\nInversa de la matriz 2: ")
    print(f"{calcular_inversa(matriz2)}")
    print("\nInversa de la matriz resultante: ")
    print(f"{calcular_inversa(matriz_resultante)}")

if __name__ == "__main__":
    main()