#Aquí quiero me de desarrolleis un programa que cuente desde un número introducido por pantalla hasta 1000, de tres en tres;
import sys

def imprimir(start):
    try:
        for i in range(int(start),1000,3):
            print(i)
    except:
        print("Introduce un valor numerico correcto")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Uso: python3 practica1 [longitud]")
    else:
        imprimir(sys.argv[1])