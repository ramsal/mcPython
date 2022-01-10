#Aquí quiero me de desarrolleis un programa con una función, que reciba una lista y un valor, y devulva las veces que aparece el valor en la lista;

def funcion(list, valor):
	cont = 0

	for i in range (len(list)):
		if list[i]==valor:
			cont += 1

	print ("El valor aparece en la lista " + str(cont) + " veces")

lista = [1, 3, 5,22, 3, 2, 1, 3, 5, 6, 7, 4, 7, 745, 6, 547, 542, 745, 67, 24]

funcion(lista, 3)
