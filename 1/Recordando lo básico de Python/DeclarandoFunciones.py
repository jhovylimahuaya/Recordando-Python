#Declarando una Funcion
"""
def Funcionjhovy():
	print ("Hello World - Hola Mundo")
	print ("Welcome - Bienvenidos")
	return "Al mundo de Jhovy"
"""
#Invocar la Funcion
"""Funcionjhovy()"""
"""Este print con la invocación de la funcion es el resultado del return de una Funcion 
conjunatmente con los print impresos antes."""
"""print (Funcionjhovy())"""
"""Este print con la invocación de la funcion sin el parentesis es el resultado de la 
dirección de memoria donde esta guardado la función Funcionjhovy - Ya que todas las
funciones en Python son igualmente objetos y print lo que hace es imprimir el valor de
la funcion y en este caso el lugar donde se guarda"""
"""print (Funcionjhovy)"""


# Definicion de una Funcion que reciba parámetros.
"""
def Funcjhovy2(parámetro1,parámetro2):
	print(parámetro1," ",parámetro2)

Funcjhovy2(123,321)
print (Funcjhovy2(123,321))
"""

#Definir una Funcion que retorne "return" un valor
	#En esta funcion no nos imprime nada mas a lo 
	#contrario le estamos diciendo que nos retorne una operación
"""
def Funcjhovy3(x):
	return x*x*x
#Por eso este print no imprime nada anterior pero si nos retorna la operación.
print (Funcjhovy3(5))
"""

# Definir una funcion que un parámetro tenga un valor por defecto.
	#Ejenplo Simple
"""	
def FuncImprimir(cadena,veces = 1):
	print (cadena * veces)
#Al invocar la funcion se imprime e ingresamos el primer parámetro se cumplira
#el operador que se imprime antes parámetro 1 por la cantidad del parámetro 2 
#el cual por defecto esta en 1 si borramos el parámetro 2 al invocar la funcion,
#inmediatamente se realizara la operacion con la cantidad que esta por defecto.
FuncImprimir("Jhovy ", 10)
"""

	#Ejemplo mas complejo
"""
def FuncPotencia(numero, veces = 1):
	valor = 1
	for i in range(veces):
		valor = valor * numero

	return valor

print (FuncPotencia(1))
"""

# Funcion con un numero variable de parametros.

def FuncMultiParam(*param):
	 resultado = 0
	 for i in param:
	 	resultado = resultado + i

	 return resultado

print (FuncMultiParam(1,2,3,4,5))