#Aquí quiero me de desarrolleis un programa que cuente desde un número introducido por pantalla hasta 1000, de tres en tres;

i= int(input('Dime un numero'))

while i < 1000:
    print(i)
    i = i + 3
if(i > 1000):
    print('El numero es muy grande')
