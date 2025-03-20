a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

print("(+) Suma a + b")
print("(-) Resta a - b")
print("(*) Multiplica a * b")
print("(/) Divide a / b")

simbolo = input("Ingresa la operación insertando el simbolo: ")

match simbolo:
    case "+":
        print ("El resultado es: ", (a+b))
    case "-":
        print ("El resultado es: ", (a-b)) 
    case "*":
        print ("El resultado es: ", (a*b))
    case "/":
        if b !=0:
            print ("El resultado es: ", (a/b))
        else:
            print ("No se puede dividir entre cero")
    case _:
        print ("Opración invalida")