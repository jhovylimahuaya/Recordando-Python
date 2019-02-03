# Calendario en python

import calendar


calendario = calendar.TextCalendar(calendar.SUNDAY)
"""
calendarioTexto = calendario.formatmonth(2019,1,2,1)

print(calendarioTexto)

calendarioHTML = calendar.HTMLCalendar(calendar.MONDAY)

calendarHTML = calendarioHTML.formatmonth(2019,10)

print(calendarHTML)

for i in calendario.itermonthdays(2019,1):
	
	print (i)

for nombreMeses in calendar.month_name:
	
	print(nombreMeses)

for nombreDias in calendar.day_name:
	
	print(nombreDias)
"""
#Siempre en for se coloca un valor mas por que cuenta solo hasta un valor menos
for mes in range(1,13):
	# Declaramos calendario
	calendario = calendar.monthcalendar(2019,mes)
#Aqui guardamos si el día viernes cumple si esta en la primera o en la segunda semana del mes
	semanaUno = calendario[0]
	semanaDos = calendario[1]
# Colocamos el condicional en el cual se tiene que cumplir lo dicho anteriormente
	if semanaUno[calendar.FRIDAY] != 0:
		
		partido = semanaUno[calendar.FRIDAY]

	else:

		partido = semanaDos[calendar.FRIDAY]
#Los porcentajes en este print se refieren a la cantidad de datos que imprimiran por variable
#Sabiendo que la primera variable imprime el nombre de los meses y
# la otra el resultado del condicional
	print ("%10s %2d" % (calendar.month_name[mes],partido))
