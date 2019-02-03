
nota1=int(input("Ingrese su Primera nota: "))
nota2=int(input("Ingrese su Segunda nota: "))
nota3=int(input("Ingrese su Tercera nota: "))
promedio=float((nota1+nota2+nota3)/3)

if promedio>=18 and promedio<=20:
	print("Excelente sigue así")

elif promedio>=15 and promedio<18:
	print("Muy bien, puedes hacerlo mejor")

elif promedio>=12 and promedio<15:
	print("Bien, Esfuerzate más")

elif promedio==11:
	print("La pasaste con lo justo, esfuerzate más")

else:
	print("Lo sentimos pero estás desaprobado")

#992393186 Principal
#973246699