import tkinter as Tk #Alias Tk

def suma():
    num1 = int(entry_num1.get()) #entry_num1 es una caja de texto 1
    num2 = int(entry_num2.get()) #entry_num2 es una caja de texto 2
    resultado = num1 + num2
    label_resultado.config(text = "Resultado: " + str(resultado)) #Asigna el texto de label_resultado

def resta():
    num1 = int(entry_num1.get()) #entry_num1 es una caja de texto 1
    num2 = int(entry_num2.get()) #entry_num2 es una caja de texto 2
    resultado = num1 - num2
    label_resultado.config(text = "Resultado: " + str(resultado)) #Asigna el texto de label_resultado

def multi():
    num1 = int(entry_num1.get()) #entry_num1 es una caja de texto 1
    num2 = int(entry_num2.get()) #entry_num2 es una caja de texto 2
    resultado = num1 * num2
    label_resultado.config(text = "Resultado: " + str(resultado)) #Asigna el texto de label_resultado

def div():
    num1 = int(entry_num1.get()) #entry_num1 es una caja de texto 1
    num2 = int(entry_num2.get()) #entry_num2 es una caja de texto 2
    resultado = num1 / num2
    label_resultado.config(text = "Resultado: " + str(resultado)) #Asigna el texto de label_resultado

app = Tk.Tk() #Ventana o formulario app, el alias Tk
app.title ("TECNOLOGICO DE ESTUDIOS SUPERIORES DE JILOTEPEC")

label_num1 = Tk.Label(text = "Ingrese el primer número: ") #label_num1 es de tipo label, se le asigna el primer valor
entry_num1 = Tk.Entry() #Captura el primer valor

label_num2 = Tk.Label(text = "Ingrese el segundo número: ") #label_num2 es de tipo label, se le asigna el segundo valor
entry_num2 = Tk.Entry() #Captura el segundo valor

label_resultado = Tk.Label(text = "*****") #label_resultado es de tipo labe, sirve para mostrar el resultado
button_suma = Tk.Button(text = "Sumar", command=suma) #boton_suma es del tipo boton, sirve para generar un boton
label_espacio = Tk.Label(text = "") #label_espacio es de tipo label, sirve para dejar espacios
button_resta = Tk.Button(text = "Restar", command=resta) #boton_resta es del tipo boton, sirve para generar un boton
label_espacio1 = Tk.Label(text = "") #label_espacio1 es de tipo label, sirve para dejar espacios
button_multi = Tk.Button(text = "Multiplicar", command=multi) #boton_multi es del tipo boton, sirve para generar un botonfica
label_espacio2 = Tk.Label(text = "") #label_espacio2 es de tipo label, sirve para dejar espacios
button_div = Tk.Button(text = "Dividir", command=div) #boton_div es del tipo boton, sirve para generar un boton

label_num1.pack() #Empaquetar para que se pueda mostrar label_num1 en pantalla
entry_num1.pack() #Empaquetar para que se pueda mostrar entry_num1 en pantalla

label_num2.pack() #Empaquetar para que se pueda mostrar label_num2 en pantalla
entry_num2.pack() #Empaquetar para que se pueda mostrar entry_num2 en pantalla

label_resultado.pack() #Empaquetar para que se pueda mostrar label_resultado en pantalla
button_suma.pack() #Empaquetar para que se pueda mostrar button_suma en pantalla
label_espacio.pack() #Empaquetar para que se pueda mostrar label_espacio en pantalla
button_resta.pack() #Empaquetar para que se pueda mostrar button_resta en pantalla
label_espacio1.pack() #Empaquetar para que se pueda mostrar label_espacio1 en pantalla
button_multi.pack() #Empaquetar para que se pueda mostrar button_multi en pantalla
label_espacio2.pack() #Empaquetar para que se pueda mostrar label_espacio2 en pantalla
button_div.pack() #Empaquetar para que se pueda mostrar button_div en pantalla

app.geometry("500x500") #Visualizar la ventana de 500 por 500 pixeles
app.mainloop() #Ciclo infinito de la ventana