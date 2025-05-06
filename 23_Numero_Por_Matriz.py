# Elaborado por Luis Carlos Ocampo Rivera
def leer_matriz():
    m = int(input("Ingrese el número de filas de la matriz: "))
    n = int(input("Ingrese el número de columnas de la matriz: "))
    matriz = []
    print("Ingrese los elementos de la matriz fila por fila")
    for i in range(m):
        fila = []
        for j in range(n):
            elemento = float(input(f"Ingrese el elemento [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz
 
def sumar_matriz(matriz, valor):
    suma = []
    for fila in matriz:
        nueva_fila = [elemento + valor for elemento in fila]
        suma.append(nueva_fila)
    return suma
 
def restar_matriz(matriz, valor):
    resta = []
    for fila in matriz:
        nueva_fila = [elemento - valor for elemento in fila]
        resta.append(nueva_fila)
    return resta

def multiplicar_matriz(matriz, valor):
    multiplicacion = []
    for fila in matriz:
        nueva_fila = [elemento * valor for elemento in fila]
        multiplicacion.append(nueva_fila)
    return multiplicacion

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Leer matriz
print("Ingrese el tamaño de la matriz")
matriz_A = leer_matriz()

# Pedir valor
valor = float(input("Ingrese el valor por el cual desea sumar, restar y multiplicar la matriz: "))

# Operaciones
resultado_suma = sumar_matriz(matriz_A, valor)
resultado_resta = restar_matriz(matriz_A, valor)
resultado_multiplicacion = multiplicar_matriz(matriz_A, valor)

# Imprimir resultados
print("\nResultado de sumar la matriz +", valor ,":")
imprimir_matriz(resultado_suma)
print("\nResultado de restar la matriz -", valor ,":")
imprimir_matriz(resultado_resta)
print("\nResultado de multiplicar la matriz *", valor ,":")
imprimir_matriz(resultado_multiplicacion)
