# Elaborado por Luis Carlos Ocampo Rivera
from sympy import symbols, Eq, solve

def resolver_ecuaciones_lineales():
    num_ecuaciones = int(input("Ingrese el número de ecuaciones lineales: "))

    variables = symbols('x1:%d' % (num_ecuaciones + 1))

    coeficientes = []
    resultados = [] 

    for i in range(1, num_ecuaciones + 1):
        coef = input(f"Ingrese los coeficientes de la ecuación {i} separados por espacios: ").split()
        coef = list(map(int, coef))
        res = int(input(f"Ingrese el resultado de la ecuación {i}: "))
        coeficientes.append(coef)
        resultados.append(res)

    ecuaciones = []
    for i in range(num_ecuaciones):
        ecuacion = Eq(sum(coeficientes[i][j] * variables[j] for j in range(num_ecuaciones)), resultados[i])
        ecuaciones.append(ecuacion)

    resultado = solve(ecuaciones, variables)

    print("Resultado:")
    print(resultado)

resolver_ecuaciones_lineales()
