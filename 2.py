#2. Contar cuantos coches son de "USA" de origen y además tienen
# tienen menos de 10 de aceleracion.

import json

from pprint import pprint

with open("coches.json") as data_file:
	data=json.load(data_file)
contador=0

for origen in data:
	if origen["Origin"] == "USA" and origen["Acceleration"] <= 10:
		contador=contador+1
print("Hay ",contador," coches de origen en USA con aceleracion inferior a 10.")
print("==================================")
print("Contar el número de coches originarios de USA con aceleracion inferior a 10")


