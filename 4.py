#4. Pedir por teclado un nombre de coche y te muestre el año de fabricacion

import json

from pprint import pprint
with open("coches.json") as data_file:
	data=json.load(data_file)
opcion=" "

while opcion != 3:
	print("Año de fabricación.")
	print("---------------------")
	print("1. Nombre de coche.")
	print("2. No tengo ni idea.")
	print("3. Salir.")
	opcion = int(input("Dime una opción correcta. "))
	if opcion == 1:
		coche=input("Dime un nombre de coche. ")
		for año in data:
			if año["Name"]==coche:
				print("---------------------")
				print("El coche elegido tiene la siguiente fecha de fabricacion: ",año["Year"])
				print("---------------------")

	elif opcion == 2:
		print("---------------------")
		print("Te muestro una ayuda.")
		print("---------------------")
		for nombre in data:
			print("*******************")
			print("Nombre y modelo: ",nombre["Name"])

	elif opcion == 3:
		print("---------------------")
		print("Adios")
		print("---------------------")

		break
	else: 
		print("Dime una opcion correcta. ")
	