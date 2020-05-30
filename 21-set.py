#Las colecciones de tipo SET no mantienen ningun orden, los elementos son unicos(no repetidos) y no se pueden modificar sus elementos

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

#Largo
print(len(planetas))

#Revisar si un elemento está presente
print("Tierra" in planetas)

#Agregar
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra") #No se pueden agregar elementos duplicados
print(planetas)

#Eliminar
planetas.remove("Tierra") #Arroja error en caso que no se encuentre el elemento
print(planetas)

planetas.discard("Jupiters")#Tambien remueve pero No arroja error en caso de no encontrarlo
print(planetas)

#Limpiar el set
planetas.clear()
print(planetas)

#Eliminar el set
del planetas