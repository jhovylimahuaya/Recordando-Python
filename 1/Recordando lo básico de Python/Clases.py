# Programación Orientada a Objetos
# Clases de Python

class miClase():
 	
 	def miMetodo(self):

 		print ("miMetodo es Mi método de la clase miClase")

 	def miMetodo2(self,texto):
 		
 		print(" > Este método hace llamado al texto: " + texto)

class miClase2(miClase):

 	def miMetodo2(self):

 		print("miMetodo2 es mi método de la clase miClase2")

 	def miMetodo(self):

 		miClase.miMetodo(self)

 		print("miMetodo es el método de la miClase2")

def main():

	objeto = miClase()

	objeto.miMetodo()

	objeto.miMetodo2(input(" > "))

	objeto2 = miClase2()

	objeto2.miMetodo2()

	objeto2.miMetodo()

if __name__ == '__main__':
	main()
