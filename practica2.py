#Aquí quiero me de desarrolleis un programa con una función, que reciba una lista y un valor, y devulva las veces que aparece el valor en la lista;
import random
import sys

def finder(nums,number):
    print("He encontrado el numero " + str(number) + " " + str(nums.count(number)) + " veces")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 practica2 [number]")
    else :
        numbers = list()
        for i in range(20):
            rand = random.randint(1, 9)
            numbers.append(rand)
        try:
            finder(numbers,int(sys.argv[1]))
        except:
            print("introduce un valor numerico correcto")