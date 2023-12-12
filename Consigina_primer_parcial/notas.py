import pandas as pd


#ruta = "consigina_primer_parcial\\insumos.csv"

# def cargar_datos():
#     with open (ruta, encoding="UTF=8") as archivo:
#         archivo = csv.reader(archivo, delimiter=",")
#         for fila in archivo:
#             print(fila)
        
#     return fila

# cargar_datos()

# def mostrar_marca():
#     with open (ruta, encoding="UTF=8") as archivo:
#         reader = csv.reader(archivo)
#         for file in reader:
#             print("Marca: " + file[2])
            
#     match:


# mostrar_marca()
# def contar_insumos():        
#     acumulador = 0
#     contador = 0
#     for cantidad in marcas:
#         acumulador += len(cantidad[2])
#         contador += 1
#     return cantidad

# contar_insumos()




# ruta = "consigina_primer_parcial\\insumos.csv"

# def cargar_datos():
#     with open (ruta, encoding="UTF=8") as archivo:
#     #     reader = csv.reader(archivo, delimiter=",")
#     #     for linea in reader:
#     #         print("ID: {0}, NOMBRE: {1}, MARCA: {2}, PRECIO: {3}, CARACTERISTICAS: {4}".format(linea[0], linea[1], linea[2], linea[3], linea[4]))
    

#         archivo = csv.reader(archivo, delimiter=",")
#         for fila in archivo:
#             print(fila)
        
#     return fila

# cargar_datos()
    

# def leer_csv(ruta:str):
#     lista_retorno = []
#     with open(ruta, "r", encoding="UTF=8") as archivo:
#         reader = csv.reader(archivo, delimiter=",")
#         for insumo in reader:
#             lista_aux = insumo
#             lista_retorno.append(lista_aux)
#             print("ID: {0} | NOMBRE: {1} | MARCA: {2} 1 PRECIO: {3} | CARACTERISTICAS: {4}".format(insumo[0], insumo[1], insumo[2], insumo[3], insumo[4]))
 
# leer_csv(ruta)
      
    #lista_insumos = leer_csv(ruta)
    #print(lista_insumos)


# def guardar_csv(ruta:str, lista_insumos:list):
#     with open(ruta, "w", encoding="UTF=8") as archivo:
#         for usuario in lista_insumos:
#             archivo.write(",".join(usuario)+"\n")
    
# lista_insumos = leer_csv(ruta)
# guardar_csv("consigina_primer_parcial\\insumos.csv", lista_insumos)
# print(lista_insumos)

