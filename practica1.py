#Aquí quiero me de desarrolleis un programa que cuente desde un número introducido por pantalla hasta 1000, de tres en tres;

i=int(input("digame el numero que vas a introducir"))

while i<1000:
	print(i)
	i=i+3
if(i>1000):
	print('El numero que has añadido es mayor al rango bro')
