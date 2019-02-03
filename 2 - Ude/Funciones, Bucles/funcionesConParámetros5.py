
# PARÁMETROS TIPO LISTA

def sumarizar(lista):

	suma=0
	for x in range(len(lista)):
		suma=suma+lista[x]
	return suma

def mayor(lista):

	may=lista[0]
	for x in range(1,len(lista)):
		if lista[x]>may:
			may=lista[x]
	return may

def menor(lista):

	men=lista[0]
	for x in range(1,len(lista)):
		if lista[x]<men:
			men=lista[x]
	return men

listaValores=[10,56,23,34,190,298]
print("Lista completa")
print(listaValores)
print("suma de los elementos: ", sumarizar(listaValores))
print("El número mayor: ", mayor(listaValores))
print("El número menor: ", menor(listaValores))