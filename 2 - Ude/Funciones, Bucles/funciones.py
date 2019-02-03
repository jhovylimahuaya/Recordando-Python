
def presentacion():
	
	print("Bienvenido a iniciando en python con Jhovy")
	print("Hoy crearemos código el cuál nos permite sumar y restar dos valores")
	print("******************************************")

def introducirDatos():
	
	global valor1
	global valor2
	valor1=int(input("Ingrese el primer valor: "))
	valor2=int(input("Ingrese el segundo valor: "))

def suma():
	
	suma = valor1 + valor2
	print("La suma de los valores es: ", suma)

def sustraccion():
	
	sustraccion = valor1 - valor2
	print("La resta de los valores es: ", sustraccion)

def finalizar():

	print("******************************************")
	print("Gracias por seguir aprendiendo con Jhovy")

# Hacemos el llamado de todas las funciones que hicimos

presentacion()
introducirDatos()
suma()
sustraccion()
finalizar()