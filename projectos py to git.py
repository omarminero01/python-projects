"""ejercicio
En una empresa donde los vendedores 
reciben el 13% de comision
el jefe quiere un programa que les ayude a calcular la comision
creando un programa que les pregunte su nombre y cuanto han vendido""" 


"""Paso 1

primero necesitamos saber  el nombre y la cantidad de ventas
almacenamos el nombre en una variable y las ventas en una segunda variable

nombre = input("Cual es tu nombre? ")
venta = input ("Cuanto se a vendido en el mes? ") 

"""


"""NOTA: hasta este punto el nombre y venta estan almacenados en dos variables!

NOTA2: Toda la informacion ingresada por el usuario son cadenas (str) por lo 
       tanto hay que convertir todos los numeros a enteros ("int") o decimales ("float") para
       poder hacer operaciones matematicas con ellos necitamos convetir todos los datos en e enteros.
"""

"""Paso 2

Ahora hay que convertir ("CASTING") la variable Venta a "int" (interger, entero)
Por que hasta el momento el usuario solo a ingresado cadenas (str)

ventas = int(ventas)
"""

"""Paso 3 

Crear una variable para calcular la comision
comision = ventas * 13 / 100

"""


"""Paso 4 

Necesitamos redondear el resultado
comision = round(comision)

"""

"""Paso 5
mostramos un mensaje en consola con los datos obtenidos de nombre y comision

print(f"Hola {nombre}, Tus comisiones de este mes son de ${comision}")

NOTA: recordar que se utilizo la formula de arriba f para poder expresar en una cadena
      con datos numericos y str.

"""

#Lineas y codigos ya generados en pytho:

nombre = input("Por favor ingresa tu nombre : ")
venta = input("Ingresa la cantidad vendida en este mes : ")
venta = int (venta)
comision = venta *13 /100
comision = round(comision)
print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
