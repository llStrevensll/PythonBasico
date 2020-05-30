#Una Tupla mantiene el orden, pero ya no se puede modificar
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

#Largo de la tupla
print(len(frutas))

#Accediendo a un elemento
print(frutas[1])

#Navegacion inversa
print(frutas[-1])

#Rango
print(frutas[0:2])#Incluyendo el indice 2

#Modificar un valor
#frutas[0] = "Naranjita"  ----#No sirve

frutasLista = list(frutas) #--> Convertir a lista
frutasLista[1] = "Platanito"
frutas = tuple(frutasLista) #--> Convertir a una tupla
print(frutas)

#Iterar una tupla
for fruta in frutas:
    print(fruta, end=" ") #para evitar el salto de linea, incluir el parametro end


#No se puede agregar ni eliminar elementos de una tupla

#Elminar tupla
del frutas

"""Ejemplo: Dada la siguiente tupla, crear una lista que sólo incluya a los números menor que 5
utilizando un ciclio for:tupla= (13, 1, 8, 3, 2, 5, 8)"""
print()
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for numero in tupla:
    if numero < 5:
        lista.append(numero)
        print(lista, end=" ")