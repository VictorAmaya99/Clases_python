import json


with open("archivos\\personas.json", "r") as file:
    lista = json.load(file)
    
print(lista)


