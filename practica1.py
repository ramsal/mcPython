#Aquí quiero me de desarrolleis un programa que cuente desde un número introducido por pantalla hasta 1000, de tres en tres;
num=int(input("Dime un numero introducido:\n"))
if num<1000:
    while num <= 1000:
        print(num)
        num=num+3
    print("1000")
else:
    print("numero no valido")
