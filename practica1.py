import os
#Aquí quiero me de desarrolleis un programa que cuente desde un número introducido por pantalla hasta 1000, de tres en tres;
os.system ("clear")
print('Bienvenido a este contador :)')
while 1>0 :
    numero = int(input('Porfavor introduzca un numero a partir del cual se sumará de tren en tres hasta mil: '))
    os.system ("clear")
    if numero <1000:
        break
    else:
        print('El numero introducido es incorrecto tiene que ser menor que 1000')

i = 1 
for numero in range(numero,1000,3):
    
    print(i ,'-' ,numero)
    i+=1