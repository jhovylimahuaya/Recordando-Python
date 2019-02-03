def cargar_paisesPoblacion():
	
	paises=[]
	for x in range(5):
		nom=input("Ingresa el nombre del país: ")
		cant=int(input("Ingresa la cantidad de habitantes: "))
		paises.append((nom,cant))
	return paises

def imprimir(paises):
	
	print("Paises y su población")
	print("*********************")
	for x in range(len(paises)):
		print(paises[x][0],paises[x][1])

def pais_masPoblacion(paises):
	pos=0
	for x in range(1,len(paises)):
		if paises[x][1]>paises[pos][1]:
			pos=x
	print("País con mayor cantidad de habitantes: ", paises[pos][0])

paises=cargar_paisesPoblacion()
print("*************************************************************")
imprimir(paises)
print("*************************************************************")
pais_masPoblacion(paises)
print("*************************************************************")