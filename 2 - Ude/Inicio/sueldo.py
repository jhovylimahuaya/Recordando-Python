
sueldo = int(input("Introduce su sueldo: "))

if sueldo > 3000:

	print("El Usuario debe pagar un porcentaje en impuestos")

if sueldo <= 3000:

	print("El Usuario esta exento de declarar su renta")

if sueldo >= 6000 and sueldo<=19999:

	print("El Usuario tiene que pagar una bonificacion de 1000 euros")

if sueldo ==20000 or sueldo ==30000:
	
	print("El Usuario paga un 10'%' de su sueldo")
