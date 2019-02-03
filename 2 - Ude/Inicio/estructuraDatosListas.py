lista=[]
for k in range(5):

	lista.append(input("Introduce un valor en la lista: "))

print("Los Primeros elementos de la lista son: " + str(lista))

#valor=int(input("Introduce el valor a modificar de la lista, coloca el índice: "))
#nuevo=input("Introduce el nuevo valor: ")
#lista[valor]=nuevo
#print("Los nuevos elementos de la lista son: " + str(lista))

#valor=int(input("Intorduce el índice en el que se insertará el nuevo: "))
#nuevo=input("Introduce el nuevo valor: ")
#lista.insert(valor, nuevo)
#print("Los nuevos elementos de la lista son: " + str(lista))

#nuevo=input("Introduce el dato de la lista a eliminar: ")
#lista.remove(nuevo)
#print("Los nuevos elementos de la lista son: " + str(lista))

nuevo=input("Introduce el valor de la lista a buscar: ")
resultado=(nuevo in lista)
if (resultado):
	print("Existe este elemento y su índice es: " + str(lista.index(nuevo)))
else:
	print("El elemento no existe en la lista ")