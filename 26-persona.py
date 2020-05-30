class Persona:
    #pass
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

"""La clase en si misma es un objeto """
#Modificar los valores
Persona.nombre = "Angel"
Persona.edad = 21

#Accede a los valores
print(Persona.nombre)
print(Persona.edad) 

#============================
#Creacion explicita de un objeto
persona = Persona("Emanuel", 22)
print(persona.nombre)
print(Persona.edad) 
print(id(persona))#direccion de memoria

#Creacion de un segundo objeto
persona2 = Persona("Steven", 23)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))#direccion de memoria