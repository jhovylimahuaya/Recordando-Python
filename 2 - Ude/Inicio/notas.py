
nota1 = int(input("Ingrese su primera nota: "))
nota2 = int(input("Ingrese su segunda nota: "))
nota3 = int(input("Ingrese su tercera nota: "))
prom=(nota1+nota2+nota3)/3

if prom>=16 and prom<=20:
	
	print("Tu promedio es excelente")

else:

	if prom>=11 and prom<=15:
		
		print("Tu promedio es aprobatorio")

	else:

		print("Estas Reprobado")
