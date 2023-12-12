import csv

# lista_personas = []

# with open ("archivos\\personas.csv", "r") as file:
#     persona = {}
#     for linea in file:
#         print(linea.split(","))
        
ruta = "archivos\\personas.csv"
#funciones parsear
def leer_csv(ruta:str):
    lista_retorno = []
    with open(ruta, "r") as archivo:
        for usuario in archivo:
            usuario = usuario.replace("\n", "")
            lista_aux = usuario.split(",")
            lista_retorno.append(lista_aux)
    return lista_retorno

def guardar_csv(ruta:str, lista_usuarios:list):
    with open(ruta, "w") as archivo:
        for usuario in lista_usuarios:
            archivo.write(",".join(usuario)+"\n")
    

lista_usuarios = leer_csv(ruta)
guardar_csv("archivos\\prueba.csv", lista_usuarios)
print(lista_usuarios)

