#! /usr/bin/python3
n = int(input("Escribe un número"))

if n >= 1000:
    print("El número debe ser menor de 1000")

while n < 1000:
    n += 3
    if(n >= 1000):
        exit()
    print(n)
