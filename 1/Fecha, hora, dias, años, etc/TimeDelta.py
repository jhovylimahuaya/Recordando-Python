from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#print(timedelta(days=365, hours=10, minutes=20))
"""
print("En un año será: "+str(datetime.now() + timedelta(days=365)))

print("En dos semanas y un día será: "+str(datetime.now()+timedelta(weeks=2, days=1)))
"""
"""
fecha = datetime.now() - timedelta(weeks=1)

formatoFecha = fecha.strftime("%A, %d %B del %Y")

print("Hace una semana fue: " + formatoFecha)
"""
# Primero vamos a declarar la variable con la fecha de hoy.
hoy = date.today()
# Aquí vamos a ingresar la fecha por teclado
fecha = date(day=int(input(">Ingrese el día: ")),
			month=int(input(">Ingrese el mes: ")),
# Aquí ingresaremos por teclado el año el cual queremos consultar
#			year=int(input(">Ingrese el año: ")),
# Aquí no va a ser necesario ingresar el año por teclado ya que
# al declarar de esta forma estamos adquiriendo el año actual
			year=hoy.year)
# Aqui ponemos la condición con la cual sabremos cuantos días
# pasaron de la fecha ingresada por teclado
if fecha < hoy:
	print("La fecha pasó hace %d días" % (hoy - fecha).days)
# Ojo else es cuando hay dos opciones pero elif nos permite hacer un condicional más
elif fecha == hoy:
	print("La fecha es Hoy")
# Aqui al declarar fecha con replace es para el siguiente ciclo el cuál
# si la fecha ingresada aun no pasó no se realice la operacion pero si pasó
# le estamos diciendo que se reemplace el año ingresado y se aumente en 1
	fecha = fecha.replace(year=hoy.year + 1)
# Aquí al haberse reemplazado ya el año se haga la siguiente operación
# fecha reemplazada - la fecha actual
diasQueFaltan= fecha - hoy
# Aquí vamos a imprimir la variable con la operacion en días 
# junto con la fecha ingresada por teclado
print("Faltan %d días para" % diasQueFaltan.days, fecha)
