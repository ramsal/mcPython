#Aquí quiero me de desarrolleis un programa con una función, que reciba una lista y un valor, y devulva las veces que aparece el valor en la lista;
#! /usr/bin/python3
numeros = [1,2,3,4,4,5,5,6]

num = int(input("Escribe un valor:"))

cont = 0

for i in range(len(numeros)):
    
    if num == int(numeros[i]):
        cont = cont +1
        

print("El número:", num ,"aparece", cont ,"veces")
