#Diccionario
d1 = {"Nombre" : "Samantha", "Edad" : 27, "Direccion" : "Tepeji del Rio", "Correo": "sama@gmail.com" }
d2 = {"Nombre" : "Maria", "Edad" : 30, "Direccion" : "Tula", "Correo": "maria35@gmail.com" }
d3 = {"Nombre" : "Jose", "Edad" : 25, "Direccion" : "Jilotepec", "Correo": "pepe@gmail.com" }

print(d1)
print(d2)
print(d3)   
 
print(d1["Nombre"]) #Samantha
print(d1.get("Direccion")) #Consultar Direccion 

#Modificar un elemento
d2["Nombre"] = "Laura" 
print(d2)

#Si el key no existe, lo añade
d1["CP"] = 54240
print(d1)

#values(). Devuelve los valores del Diccionario
print(list(d1.values()))
print(list(d2.values()))
print(list(d3.values()))

#popitem. Elimina el ultimo elemnto del Diccionario
d1.popitem()
print(d1)

#pop. Se puede eliminar un elemento en particular
salida = d1.pop("Edad")
print(d1)

#update. Llama un Diccionario y tiene como entrada otro Diccionario
t1 = {"A" : 100, "B" : 200}
t2 = {"C" : 50, "D" : 400}
t1.update(t2)
print(t1)
