
import os
from os import path

import datetime

from datetime import date, time, timedelta, timezone

import time

def main():

#	print(os.name)

#	print("El archivo existe: %s" % str(path.exists("archivoCreado.txt")))

#	print("Es un archivo: %s" % str(path.isfile("archivoCreado.txt")))

#	print("Es un directorio: %s" % str(path.isdir("archivoCreado.txt")))

#	print("El archivo está en el siguiente directorio: %s" % path.realpath("archivoCreado.txt"))

#	print("El directorio y el nombre es: %s" % str(path.split(path.realpath("archivoCreado.txt"))))
# Con [0] estamos diciendo que nos imprima solo el primer atributo
#	print("El directorio y el nombre es: %s" % str(path.split(path.realpath("archivoCreado.txt"))[0]))
# Con [1] estamos diciendo que nos imprima solo el segundo atributo
#	print("El directorio y el nombre es: %s" % str(path.split(path.realpath("archivoCreado.txt"))[1]))

	tiempo = time.ctime(path.getmtime("archivoCreado.txt"))
# Son distintas formatos en que se imprime en estos print. 
	print("El archivo fue modificado por ultima vez el: ", tiempo)

	print("El archivo fue modificado por ultima vez el: ", datetime.datetime.fromtimestamp(path.getmtime("archivoCreado.txt")))

	tTranscurrido = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("archivoCreado.txt"))

	print("Ha pasado %s desde que se modificó por ultima vez el archivo: " % str(tTranscurrido),str(path.split(path.realpath("archivoCreado.txt"))[1]))

	print("Han transcurrido %s segundos" % str(tTranscurrido.total_seconds()))

if __name__ == '__main__':
	main()