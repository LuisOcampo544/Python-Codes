import random
 
def numeros(): 
    x = random.randint(0,5)
    if x == 1:
         print(x , "Pierdes")
    else:
        print(x , "Ganas")
  
ruleta = input("Presione la tecla 1: ")

match ruleta:
    case "1": 
        numeros() 
