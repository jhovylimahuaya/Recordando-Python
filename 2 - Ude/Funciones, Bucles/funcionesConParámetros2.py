# RETORNO DE DATOS
def retorno_superficie(lado):

	su=lado*lado
	return(su)

va=int(input("Introduce el valor del cuadrado: "))
superficie=retorno_superficie(va)
print("La superficie del cuadrado es: ", superficie)