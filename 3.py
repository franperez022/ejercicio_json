#3. Busqueda avanzada de un coche clásico
#introduce por teclado cuantos cv tiene.
#introduce por teclado cuantos cilindros tiene
#introduce por teclado de que origen es
#si está mostrar la información del coche, si no "Coche no registrado" volver a probar
import json

from pprint import pprint

with open("coches.json") as data_file:
	data=json.load(data_file)
print("------------------")
print("Busqueda Avanzada.")
print("------------------")
cv=int(input("Dime cuantos cv (caballos) tiene el coche. "))
ncilindros=int(input("Dime cuantos cilindros tiene el coche. "))
origen=input("Dime el origen. ")
peso=int(input("Dime el peso en lbs. "))
print("------------------")
encontrado=False
for coches in data:
	if coches["Horsepower"] == cv and coches["Cylinders"] == ncilindros and coches["Origin"] == origen and coches["Weight_in_lbs"] == peso:
		print("Su coche es: ")
		print ("Marca y modelo: ",coches["Name"])
		print ("Millas: ",coches["Miles_per_Gallon"])
		print ("Cilindros: ",coches["Cylinders"])
		print ("Desplazamiento: ",coches["Displacement"])
		print ("Cv: ",coches["Horsepower"])
		print ("Peso: ",coches["Weight_in_lbs"])
		print ("Aceleracion: ",coches["Acceleration"])
		print ("Año: ",coches["Year"])
		print ("Origen: ",coches["Origin"])
		encontrado=True
if not encontrado:
	print("------------------")
	print("COCHE NO REGISTRADO.")
	print("------------------")
