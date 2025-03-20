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
       print("Numero de estudiante invalido")
else:
   print("Periodo invalido")