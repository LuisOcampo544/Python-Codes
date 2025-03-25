n = int(input("Ingresa un valor: "))  
x = 0
e = 2
for i in range(1, n + 1):
    x += i ** e
    e += 1
r = x / n
print("Resultado: ", r)
