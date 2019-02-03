# Creando sentencias condicionales en Python

# Sentencia if
"""
#Primero declaramos una variable
texto = "Jhovy"

if texto == "Jhovy":
	print ("Bienvenido " + texto)
"""
#Sentencia if - else
"""
texto = input("> ")

if texto == "Jhovy":
	print ("Escribiste tu Nombre")
else:
	print ("No escribiste tu Nombre")
"""

# Sentencia if - elif - else

numero = int(input("> "))

if numero >0:
	print("Es un número positivo")
elif numero <0:
	print("Es un número negativo")
else:
	print("Es cero")