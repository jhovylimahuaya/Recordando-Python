# PARÁMETROS
def mostrar_mensaje(mensaje):
# fucniones con parámetros simples.
	print("*******************************************************************")
	print(mensaje)
	print("*******************************************************************")

def sumar():

	valor1=int(input("Ingrese el primer valor: "))
	valor2=int(input("Ingrese el srgundo valor: "))
	suma=valor1+valor2
	print("La suma de los valores es: ", suma)

mostrar_mensaje("Código de suma de dos valores")
sumar()