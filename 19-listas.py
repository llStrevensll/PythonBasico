nombres = ["Angel", "Emanuel", "Steven", "Rodriguez", "Castro"]
print(nombres)

#Conocer el largo-tamaño de la lista
print(len(nombres))

#Elemento 0
print(nombres[0])
print(nombres[1])
#print(nombres[5])#Indice fuera de rango

#Navegacion inversa
print(nombres[-1])
print(nombres[-2])

#Imprimir rango
print(nombres[0:2])#sin incluir el indice 2

#Imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:3])#sin incluir el indice 3

#Imprimir los elementos hasta el final, desde el indice proporcionado
print(nombres[1:])

#Cambiar los nombres de una lista
nombres[3] = "Strevens"
print(nombres)

#Iterar la lista
for nombre in nombres:
    print(nombre)
    
#Revisar si existe un elemento en la lista
if "Angell" in nombres:
    print("Angel si existe en la lista")
else:
    print("El elementos buscado no existe en la lista")
    
#Agregar nuevo elemento
nombres.append("StrevensFull")
print(nombres)

#Insertar un nuevo elemento en el indice indicado
nombres.insert(1, "Kael")
print(nombres)

#Remover un elemento
nombres.remove("Kael")
print(nombres)

#Remover el ultimo elemento de nuestra lista
nombres.pop()
print(nombres)

#Limpiar los elementos de nuestra lista
nombres.clear()
print(nombres)

#Eliminar por completo la lista 
del nombres
#print(nombres)

#Ejemplo iterar lista de 0 a 10, imprimir numeros solo divisible entre 3
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista:
    if numero % 3 == 0:
        print("El numero : ", numero, "es divisible por 3")
    else:
        continue
        print("El numero NO es divisible por 3")
        
    