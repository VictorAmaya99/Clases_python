import json

with open("heroes.json", "r") as file:
    lista = json.load(file)
    
print(lista)