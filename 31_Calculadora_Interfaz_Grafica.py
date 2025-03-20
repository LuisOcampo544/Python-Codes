import tkinter
from tkinter import font

# Funciones

def insertar_boton0():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "0")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "0")

def insertar_boton1():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "1")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "1")

def insertar_boton2():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "2")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "2")

def insertar_boton3():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "3")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "3")

def insertar_boton4():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "4")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "4")

def insertar_boton5():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "5")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "5")

def insertar_boton6():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "6")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "6")

def insertar_boton7():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "7")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "7")

def insertar_boton8():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "8")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "8")

def insertar_boton9():
    if caja1.focus_get() == caja1:
        caja1.insert(tkinter.END, "9")
    elif caja2.focus_get() == caja2:
        caja2.insert(tkinter.END, "9")

def operaciones():
        valor1 = float(caja1.get())
        valor2 = float(caja2.get())
        operacion = caja_operacion.get()
        
        if operacion == "+":
            resultado = valor1 + valor2 

        elif operacion == "-":
            resultado = valor1 - valor2

        elif operacion == "*":
            resultado = valor1 * valor2 

        elif operacion == "/":
            if valor2 != 0:
                resultado = valor1 / valor2 
            else:
                caja_resultado.delete(0,tkinter.END)
                caja_resultado.insert(0, "Error: Division entre 0")
                return
            
        caja_resultado.delete(0, tkinter.END)
        caja_resultado.insert(0, resultado) 

def limpiar():
    caja1.delete(0, tkinter.END)
    caja2.delete(0, tkinter.END)  
    caja_operacion.delete(0, tkinter.END)  
    caja_resultado.delete(0, tkinter.END)

# Ventana principal

ventana = tkinter.Tk()
ventana.title ("Calculadora")
ventana.geometry("300x320")
ventana.configure(bg = "#808080")

# Botones

boton0 = tkinter.Button(ventana, text = "0", width = 4, height = 2, command = insertar_boton0)
boton0.grid(row = 1, column = 1, padx = 5, pady = 5)

boton1 = tkinter.Button(ventana, text = "1", width = 4, height = 2, command = insertar_boton1)
boton1.grid(row = 1, column = 2, padx = 5, pady = 5)

boton2 = tkinter.Button(ventana, text = "2", width = 4, height = 2, command = insertar_boton2)
boton2.grid(row = 1, column = 3, padx = 5, pady = 5)

boton3 = tkinter.Button(ventana, text = "3", width = 4, height = 2, command = insertar_boton3)
boton3.grid(row = 1, column = 4, padx = 5, pady = 5)

boton4 = tkinter.Button(ventana, text = "4", width = 4, height = 2, command = insertar_boton4)
boton4.grid(row = 1, column = 5, padx = 5, pady = 5)

boton5 = tkinter.Button(ventana, text = "5", width = 4, height = 2, command = insertar_boton5)
boton5.grid(row = 2, column = 1, padx = 5, pady = 5)

boton6 = tkinter.Button(ventana, text = "6", width = 4, height = 2, command = insertar_boton6)
boton6.grid(row = 2, column = 2, padx = 5, pady = 5)

boton7 = tkinter.Button(ventana, text = "7", width = 4, height = 2, command = insertar_boton7)
boton7.grid(row = 2, column = 3, padx = 5, pady = 5)

boton8 = tkinter.Button(ventana, text = "8", width = 4, height = 2, command = insertar_boton8)
boton8.grid(row = 2, column = 4, padx = 5, pady = 5)

boton9 = tkinter.Button(ventana, text = "9", width = 4, height = 2, command = insertar_boton9)
boton9.grid(row = 2, column = 5, padx = 5, pady = 5)

boton_suma = tkinter.Button(ventana, text = "+", width = 4, height = 2, command = lambda: caja_operacion.insert(tkinter.END, "+"))
boton_suma.grid(row = 1, column = 6, padx = 5, pady = 5)

boton_resta = tkinter.Button(ventana, text = "-", width = 4, height = 2, command = lambda: caja_operacion.insert(tkinter.END, "-"))
boton_resta.grid(row = 2, column = 6, padx = 5, pady = 5)

boton_multi = tkinter.Button(ventana, text = "*", width = 4, height = 2, command = lambda: caja_operacion.insert(tkinter.END, "*"))
boton_multi.grid(row = 3, column = 6, padx = 5, pady = 5)

boton_div = tkinter.Button(ventana, text = "/", width = 4, height = 2, command = lambda: caja_operacion.insert(tkinter.END, "/"))
boton_div.grid(row = 4, column = 6, padx = 5, pady = 5)

boton_igual = tkinter.Button(ventana, text = "=", fg = "White", width = 4, height = 2, command = operaciones)
boton_igual.grid(row = 5, column = 6, padx = 5, pady = 5)
boton_igual.configure(bg = "#CC7722")

boton_ac = tkinter.Button(ventana, text = "AC", fg = "White", width = 4, height = 2, command = limpiar)
boton_ac.grid(row = 6, column = 6, padx = 5, pady = 5)
boton_ac.configure(bg = "#CC7722")

# Cajas de texto

caja1 = tkinter.Entry(ventana, width = 7, font = ("Helvetica 16"))
caja1.grid(row = 4, column = 1, columnspan = 2, padx = 5, pady = 5)

caja2 = tkinter.Entry(ventana, width = 7, font = ("Helvetica 16"))
caja2.grid(row = 4, column = 4, columnspan = 2, padx = 5, pady = 5)

caja_operacion = tkinter.Entry(ventana, width = 3, font = ("Helvetica 16"), justify = "center")
caja_operacion.grid(row = 4, column = 3, padx = 5, pady = 5)

caja_resultado = tkinter.Entry(ventana, width = 20, font = ("Helvetica 16"))
caja_resultado.grid(row = 6, column = 1, columnspan = 5, padx = 5, pady = 5)

# Etiquetas

etiqueta1 = tkinter.Label(ventana, text = "Valor 1", width = 7, font = ("Helvetica 15"))
etiqueta1.grid(row = 3, column = 1, columnspan = 2, padx = 5, pady = 5)
etiqueta1.configure(bg = "#808080")

etiqueta2 = tkinter.Label(ventana, text = "Valor 2", width = 7, font = ("Helvetica 15"))
etiqueta2.grid(row = 3, column = 4, columnspan = 2, padx = 5, pady = 5)
etiqueta2.configure(bg = "#808080")

etiqueta_resultado = tkinter.Label(ventana, text = "Resultado", width =12, font = ("Helvetica 15"))
etiqueta_resultado.grid(row = 5, column = 2, columnspan = 3, padx = 5, pady = 5)
etiqueta_resultado.configure(bg = "#808080")

ventana.mainloop()