import json

# with open("Desafio_Stark\\data_stark.json", "r") as file:
#     lista =json.load(file)

# print(lista)

#rutacvs = "archivos\\personas.csv"
rutajson = "archivos\\personas.json"
#funciones parsear
# def leer_csv(ruta:str):
#     lista_retorno = []
#     with open(ruta, "r") as archivo:
#         for usuario in archivo:
#             usuario = usuario.replace("\n", "")
#             lista_aux = usuario.split(",")
#             lista_retorno.append(lista_aux)
#     return lista_retorno

# def guardar_csv(ruta:str, lista_usuarios:list):
#     with open(ruta, "w") as archivo:
#         for usuario in lista_usuarios:
#             archivo.write(",".join(usuario)+"\n")
            
def leer_json(ruta:str)->list:
    with open(ruta, "r") as archivo:
        diccionario_usuarios = json.load(archivo)
    return diccionario_usuarios["usuarios"]
    
def guardar_json(ruta:str, lista_usuarios:list)->None:
    with open(ruta, "w") as archivo:
        json.dump(lista_usuarios, archivo, indent=4)

lista_usuarios = leer_json(rutajson)
guardar_json("archivos\\prueba.json", lista_usuarios)
    
print(lista_usuarios)


