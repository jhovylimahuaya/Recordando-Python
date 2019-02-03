
def cargar():
	
	diccionario={}
	continua="s"
	while continua=="s":
		espa=input("Ingrese la palabra en español que va a buscar: ")
		ing=input("Ingrese la palabra en ingles que va a buscar: ")
		diccionario[espa]=ing
		continua=input("Quiere cargar otra palabra: [s/n]")
	return diccionario

def imprimir(diccionario):
	
	print("Listado completo del Diccionario")
	print("********************************")
	for ingles in diccionario:
		print(ingles, diccionario[ingles])

def consulta_palabra(diccionario):
	
	pal=input("Ingrese la palabra en castellano a consultar: ")
	if pal in diccionario:
		print("En inglés significa: ", diccionario[pal])


# Bloque principal

diccionario=cargar()
imprimir(diccionario)
print("*****************************")
consulta_palabra(diccionario)
