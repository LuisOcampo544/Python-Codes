acu = 0
while True: #Al menos una vez
    n1 = (input("Teclea un número o Presione X para salir del programa: ")) 
    if (n1 == "x"):
        break #Rompe el ciclo  
    else:  
        acu = acu + int(n1) #Toma n1 como entero

        #Esta fuera del ciclo lo siguiente
if (acu > 0):
    print ("El resultado final del acumulador es ---> ", acu)
else:
    print ("Se pulso X para salir del bucle")
