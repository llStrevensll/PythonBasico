num1 = 0
numeros =[]
for num1 in range(11):
    print(num1)
    if num1>0 and num1%3 == 0:
        num2=num1+1
        numeros.insert(num2, num1)
    num1=num1+1
print(numeros)