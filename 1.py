#1. Listar todos los coches, mostrar nombre, modelo aceleracion y numero de cilindros.

import json

from pprint import pprint

with open("coches.json") as data_file:
	data=json.load(data_file)


for nombre in data:
	print("==========================================")
	print("Nombre y modelo: ",nombre["Name"])
	print("Numero de cilindros: ",nombre["Cylinders"])
	print("Numero de aceleracion: ",nombre["Acceleration"])
	print("********************************************")
	print("Listando todos los coches registrados en este fichero.")
	print("********************************************")