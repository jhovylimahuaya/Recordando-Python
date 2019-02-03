from datetime import time
from datetime import date
from datetime import datetime

def main():

	hoy = date.today()

	print(hoy)

	print(" el dia es: ",hoy.day," el mes es: ",hoy.month," el anio es: ",hoy.year)

	print("La información completa del día es: ", hoy.weekday())

	hoy = datetime.today()

	print(hoy)

	hora = datetime.time(datetime.now())

	print(hora)

	dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

	nroDia = date.weekday(hoy)

	print("El numero del día es: %d" %nroDia)

	print("El día es: %s" %dias[nroDia])

if __name__ == '__main__':
	main()