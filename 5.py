#5 Adivina el coche
"""Le pregunto al usuario algunas caracteristicas sobre mi coche si acierta las dos 
le digo 'introduce el nombre' si no es 'fallaste' y si no acierta las dos caracteristica
'por poco' o 'te colaste' segun el valor añadido"""
import json
import random
from pprint import pprint
lista=()
with open("coches.json") as data_file:
	data=json.load(data_file)
coche=random.choice(data)
nombre=coche["Name"]
print("Pista: ""Cuatro primeras letras del nombre y desplazamiento.")
print (coche["Name"][0:4]) 
print (coche["Displacement"]) 
print("Tranquilo si no sabes jugar puedes ejecutar el ejercicio 1 para ayudarte")
print("---------------------")
print("Que comience el juego.")
print("---------------------")
print("Yo pienso un modelo de coche y tu lo tienes que adivinar")
cilindros=int(input("Cuantos cilindros crees que tiene mi coche. "))
print("---------------------")
if coche["Cylinders"] == cilindros:
	print("Correcto")
elif coche["Cylinders"] != cilindros and coche["Cylinders"] > cilindros:
	print("por poco")
elif coche["Cylinders"] != cilindros and coche["Cylinders"] < cilindros:
	print("Te colaste")	
aceleracion=float(input("Cuanta aceleracion crees que tiene mi coche. "))
if coche["Acceleration"] == aceleracion:
	print("Correcto")
	if coche["Acceleration"] == aceleracion and coche["Cylinders"] == cilindros:
		resuelve=input("Dime el nombre: ")
		if resuelve == nombre:
			print("---------------------")
			print("Lo acertaste, tú ganas!!!!!")
			print("------------------")
		elif resuelve != nombre:	
			print("---------------------")
			print("Casi lo aciertas, muy buena partida!!!!!")
			print("------------------")
elif coche["Acceleration"] != aceleracion and coche["Acceleration"] > aceleracion:
	print("por poco")
elif coche["Acceleration"] != aceleracion and coche["Acceleration"] < aceleracion:
	print("Te colaste")	
	if coche["Acceleration"] != aceleracion and coche["Cylinders"] != cilindros:
		print("---------------------")
		print("No lo acertaste, gano yo!!!!!")
		print("---------------------")
