#Shell utilities en Python

import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
	
	if(path.exists("archivoModificado.txt")):

		src = path.realpath("archivoModificado.txt")

#		rutaArchivo, nombreArchivo = path.split(src)

#		print("El archivo esta en el siguiente directorio: %s" % rutaArchivo)
#		print("El nombre del archivo es: %s" % nombreArchivo)

#		os.rename("archivoCreado.txt", "archivoModificado.txt")

#	archivoModificado = src + ".bak"

#	shutil.copy(src, archivoModificado)

#	shutil.copystat(src, archivoModificado)

		#ruta, nombre = path.split(path.realpath("archivoModificado.txt"))

		#shutil.make_archive("Comprimido", "zip", ruta)

		with ZipFile("comprimido.zip", "w") as nuevozip:

			nuevozip.write("archivoModificado.txt")
			nuevozip.write("archivoModificado.txt.bak")

	pass

if __name__ == '__main__':
	main()