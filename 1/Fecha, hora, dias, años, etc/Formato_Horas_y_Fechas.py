# Dando formato a las horas y las fechas en Python

from datetime import datetime

def main():
	
	hoy = datetime.now()
# Nos imprime en el formato normal de la Fecha y las Hora
	print(hoy)

# Nos imprime %Y el año completo y %y simplemente la abreviación del año
# Ejemplo: %Y > 2019 y %y > 19
#	print(hoy.strftime("%Y" " - " "%y"))
# Nos imprime %B el mes completo y %b simplemente la abreviación del mes
# Ejemplo: %B > January y %b > Jan
#	print(hoy.strftime("%B" " - " "%b"))
# Nos imprime el numero de la fecha que nos encontramos
#	print(hoy.strftime("%d"))
# Nos imprime %A el día completo y %a simplemente la abreviación del día
# Ejemplo: %A > Monday y %a >Mon 
#	print(hoy.strftime("%A" " - " "%a"))
# Vamos a imprimir la fecha con el siguiente formato
# Nombre del día, número del día, el mes, y el año; como para un documento
#	print(hoy.strftime("%a, %d %B %Y"))

# Nos imprime %I la hora en formato 12 horas y %H la hora en formato 24 horas
# Ejemplo: %I > 04 y %y > 16
#	print(hoy.strftime("%I - %H"))
# Nos imprime %M los minutos
#	print(hoy.strftime("%M"))
# Nos imprime %S los segundos
#	print(hoy.strftime("%S"))
# Vamos a imprimir la hora con distintos formatos
# Ejemplo: Hora: Minuto: Segundo en ambos formatos en 12 y 24 horas
# En el formato de 12 horas va a ser necesario colocar %p para saber si es AM o PM
	print(hoy.strftime("%I:%M:%S %p"))
# Formato de 24 horas	
	print(hoy.strftime("%H:%M:%S"))

if __name__ == '__main__':
	main()