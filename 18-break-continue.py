#Imprimir solo la primera letra a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
else:
    print("Fin del for")  
    

#Imprimir sólo números pares
"""for i in range(6):
    if i%2 == 0:
        print(i)  """
        
#Imprimir sólo números pares
for i in range(6):
    if i%2 != 0:
        continue
    print(i) 
        
