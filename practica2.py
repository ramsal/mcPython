#Aquí quiero me de desarrolleis un programa con una función, que reciba una lista y un valor, y devulva las veces que aparece el valor en la lista;
def contador(lista,a):
    print(lista.count(a))
#Parte Main
lista=[1,2,3,5,1,4,6,9]
num=int(input("Dime que numero buscas"))

contador(lista,num)
