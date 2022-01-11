#Aquí quiero me de desarrolleis un programa con una función, que reciba una lista y un valor, y devulva las veces que aparece el valor en la lista;

def funcionLista(lista, valor):
	return lista.count(valor)


lista = [1,2,3,4,4,5,6,2,3,2,2]

print (funcionLista(lista,2))
