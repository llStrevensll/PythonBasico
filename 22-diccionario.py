#Un diccionaro está compuesto de llave,valor (ket, value)
diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Databse Management System"
}

print(diccionario)

#Largo
print(len(diccionario))

#Accediendo a un elemento por medio de su llave (key)
print(diccionario["IDE"])

#Otra forma de acceder al elemento
print(diccionario.get("IDE"))

#Modificando valores
diccionario["IDE"]= "Integrated development enviroment"
print(diccionario)

#Iterar
for termino in diccionario: #Imprime las llaves
    print(termino)
    
for termino in diccionario: #Imprime el valor de las llaves
    print(diccionario[termino])

print("==============")

for valor in diccionario.values(): #Imprimir valor de las llaves con funcion .values
    print(valor)
    
#Comprobando existencia de un elemento
print("IDE" in diccionario)

#Agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

#Remover elementos
diccionario.pop("DBMS")
print(diccionario)

#Limpiar
diccionario.clear()
print(diccionario)

#Eliminar
del diccionario
