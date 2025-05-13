def X_Tabla():
    x = int(input('Dime que tabla de multiplicar deseas realizar: '))
    a = 1;
    while a <= 10: #Ciclo
        print(f"{x} x {a} = {x * a}")
        a += 1  

def Par_Impar():
    print ('Número Par o Impar')
    N1 = int(input('Dame un número: '))
    if N1 % 2 == 0:
        print ('El número es par') 
    else:
        print ('El número es impar')
 
def If_Anidado():
    x = int(input('Ingresa tu calificación --> '))
    if x > 100:
        print('Calificación no valida')
    elif x == 100:
        print('Excelente, felicidades')
    elif x <= 99 and x >= 90:
        print('Muy bien')
    elif x <= 89 and x >= 80:
        print('Bien')
    elif x <= 79 and x >= 70:
        print('Alumno regular')
    else:
        print('Alumno no aprobado')

def Formula():
    n = int(input("Ingresa un valor: "))
    x = 0
    e = 2
    for i in range(1, n + 1):
        x += i ** e
        e += 1
    r = x / n
    print("Resultado: ", r)

def No_Control():
    import datetime
    fecha=datetime.datetime.now()
    import datetime
    año=datetime.datetime.strftime( fecha,"%Y")
    x=int (input ("Ingresa el periodo en el que ingresaste: "))

    if x==1 or x ==2:
        num=int (input ("Ingresa tu numero de estudiante: ")) 
        if num<=999:
            numero = input ("Ingresa la carrera a la que perteneces 1.-Ing. Industrial, 2.-TIC'S,3.-Ing. en sistemas computacionales,  4.-Ing. Quimica,5.-Ing.Civil,6.-Ing. Mecatronica,7.-Ing. Electrica,8.-Ing. Logistica,9.-Lic. Administracion:  ")
            match numero:
                case "1":
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(1)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(1)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num<= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(1)+str(num2)
                        print("Tu matricula es: ",a)
                case "2":
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(2)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(2)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num>= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(2)+str(num2)
                        print("Tu matricula es: ",a)
                case "3":
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(3)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(3)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num>= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(3)+str(num2)
                        print("Tu matricula es: ",a)
                case "4":
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(4)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(4)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num>= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(4)+str(num2)
                        print("Tu matricula es: ",a)
                case "5" :
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(5)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(5)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num>= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(5)+str(num2)
                        print("Tu matricula es: ",a)
                case "6":
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(6)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(6)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num>= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(6)+str(num2)
                        print("Tu matricula es: ",a)
                case "7":
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(7)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(7)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num>= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(7)+str(num2)
                        print("Tu matricula es: ",a)
                case "8":
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(8)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(8)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num>= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(8)+str(num2)
                        print("Tu matricula es: ",a)
                case "9":
                    if num >= 10 and num<=99:
                        num1=f"0{num}"
                        a = str(año)+str(x)+str(9)+str(num1)
                        print("Tu matricula es: ",a)
                    elif num <= 999 and num>=100 :
                        num2=f"{num}"
                        a = str(año)+str(x)+str(9)+str(num2)
                        print("Tu matricula es: ",a)
                    elif num>= 1 and num<=9: 
                        num2=f"00{num}"
                        a = str(año)+str(x)+str(9)+str(num2)
                        print("Tu matricula es: ",a)                                 
        else:
            print("Número de estudiante invalido")
    else:
        print("Periodo invalido")

def Salir():
    exit()

def Opciones():
    print ("")
    print ("1.- X Tabla")
    print ("2.- Par O Impar")
    print ("3.- If Anidado")
    print ("4.- Formula")
    print ("5.- No Control")
    print ("6.- Salir")

while True: 

    Opciones()

    eleccion = input("Elige que programa deseas realizar: ")

    match eleccion:
        case "1":
            X_Tabla()
        case "2":
            Par_Impar()
        case "3":
            If_Anidado()
        case "4":
            Formula()
        case "5":
            No_Control()
        case "6":
            Salir()
        case _:
            print ("Elección invalida")
