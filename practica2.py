#Aquí quiero me de desarrolleis un programa con una función, que reciba una lista y un valor, y devulva las veces que aparece el valor en la lista;

def Llenar_lista():
    li=[]
    for x in range(10):
        numero=int(input("Ingrese un numero:"))
        li.append(numero)
    return li


def imprimir_numeroR(li):
    n=int(input("Ingrese un numero de la lista para ver cuantas veces se repite:"))
    
    print ("el numero ese se repite-->", li.count(n))
   
        
lista=Llenar_lista()
imprimir_numeroR(lista)
