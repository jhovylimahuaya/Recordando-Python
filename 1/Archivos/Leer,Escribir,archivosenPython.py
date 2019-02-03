def main():
# Ojo w+ es para escribir y/o modificar archivo creado
	archivo = open("archivoCreado.txt", "w+")
# Ojo a+ es para sobreescribir en le archivo creado
#	archivo = open("archivoCreado.txt", "a+")

	for i in range(10):

		archivo.write("Esta es la línea: %d\n" % (i+1))

	archivo.close() 
# Ojo r solamente es para leer ya que significa read
	archivo = open("archivoCreado.txt", "r")
# En esta condicion le decimos si lo que declaramos es igual al valor, cumpla la operacion
	if archivo.mode == "r":
		# Declaramos una nueva variable diciendo que nos realice la accion de lectura
		lineasArchivo = archivo.readlines()
	# Realizamos un for en el cual va a imprimir la operación que declaramos anteriormente 
		for linea in lineasArchivo:
			
			print(linea)

if __name__ == '__main__':
	main()