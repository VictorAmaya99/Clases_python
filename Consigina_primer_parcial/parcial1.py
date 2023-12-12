# Administración de Insumos de una Tienda de Mascotas

# Se solicita desarrollar un programa para administrar los insumos de una
# tienda de mascotas. Para ello, se dispone de un archivo CSV con el
# siguiente formato:
    
# ID,NOMBRE,MARCA,PRECIO,CARACTERISTICAS

# 1,Alimento para perros,Pedigree,$12.99,Sabor delicioso~Nutrición
# equilibrada~Contiene vitaminas y minerales
   

import csv 
import re
import pandas as pd

# El programa debe ofrecer un menú con las siguientes opciones:



# 1. Cargar datos desde archivo: Esta opción permite cargar el contenido
# del archivo "Insumos.csv" en una colección, teniendo en cuenta que
# las características de los insumos deben estar en un tipo de colección
# integrada.

ruta = "consigina_primer_parcial\\insumos.csv"

def csv_como_lista_dict(ruta):
    separador = ","
    with open(ruta, encoding="UTF=8") as archivo:
        #next(archivo)
        insumos = []
        for linea in archivo:
            linea = linea.rstrip("\n")
            columnas = linea.split(separador)
            id = columnas[0]
            nombre = columnas[1]
            marca = columnas[2]
            precio = columnas[3]
            caract = columnas[4]
            insumos.append({
                "Id": id,
                "Nombre": nombre,
                "Marca": marca,
                "Precio": precio,
                "Caracteristicas": caract,
            })
        return insumos

def cargar_datos():
    insumos = csv_como_lista_dict(ruta)
    for insumo in insumos:
        id = insumo["Id"]
        nombre = insumo["Nombre"]
        marca = insumo["Marca"]
        precio = insumo["Precio"]
        caract = insumo["Caracteristicas"]
        print("Id: ", id, "|", "Nombre: ", nombre, "|", "Marca: ", marca, "|", "Precio: ", precio, "|", "Caracteristicas: ", caract)
        #print(f"Id: {id} | Nombre: {nombre} | Marca: {marca} | Precio: {precio} | Caracteristicas: {caract}")
        
cargar_datos()

# 2. Listar cantidad por marca: Muestra todas las marcas y la cantidad
# de insumos correspondientes a cada una.

marcas = []

def lista_cantidad_por_marca():
    insumos = csv_como_lista_dict(ruta)
    for insumo in insumos:
        marcas.append(insumo["Marca"])
        print("Marca: ", insumo["Marca"], "|" , "Cantidad: ", len(insumo["Marca"]))
        
lista_cantidad_por_marca()
  
print("------------------------------")
  
# 3. Listar insumos por marca: Muestra, para cada marca, el nombre y
# precio de los insumos correspondientes.

def lista_insumos_marca():
    insumos = csv_como_lista_dict(ruta)
    for insumo in insumos:
        print("Marca: ", insumo["Marca"], "|" , "Precio: ", insumo["Precio"])

lista_insumos_marca()      
  
print("------------------------------")

# 4. Buscar insumo por característica: El usuario ingresa una
# característica (por ejemplo, "Sin Granos") y se listarán todos los
# insumos que poseen dicha característica.

def insumo_caracteristica():
    insumos = csv_como_lista_dict(ruta)
    lista_insumos = []
    palabra = input("Ingrese lo que busca: ")
    lista_insumos.append(palabra)
    for palabra in insumos:

# 5. Listar insumos ordenados: Muestra el ID, descripción, precio, marca
# y la primera característica de todos los productos, ordenados por
# marca de forma ascendente (A-Z) y, ante marcas iguales, por precio
# descendente.


def insumos_ordenados():
    insumos = csv_como_lista_dict(ruta)
    ordenados = list(sorted(set(map(lambda ins:ins["Marca"], insumos))))
    for marca in ordenados:
        print(marca)

insumos_ordenados()

# def marcas_iguales_por_precio():
#     insumos = csv_como_lista_dict(ruta)
#     iguales_precio = list(filter(lambda ins:ins["Marca"] == ins["Marca"] and ins["Precio"] > ins["Precio"], len(insumos)))
#     print(iguales_precio)
# marcas_iguales_por_precio()


# def insumos_ordenados(lista:list, key: str, ascendente: True):
   
#    tam = len(insumos)
#    for i in range(tam-1):
#         for j in range(i+1, tam):
#                 if (ascendente and lista[i][key] > lista[j][key]) or (not ascendente and lista[i][key] < lista[j][key]):
#                     aux = lista[i]
#                     lista[i] = lista[j]
#                     lista[j] = aux
#                     #print(aux)
                    
#             #return aux

# insumos = csv_como_lista_dict(ruta)
# def mostrar_insumo(insumo:dict):
#     print(f"{insumo['Id']}  {insumo['Nombre']}  {insumo['Marca']}  {insumo['Precio']}  {insumo['Caracteristicas']}")

# def mostrar_insumos(insumos:list):
#     for insumo in insumos:
#         mostrar_insumo(insumo)

# print(mostrar_insumos(insumos))
insumos = csv_como_lista_dict(ruta)

def marcas_iguales_por_precio(lista:list):
    tam = len(insumos)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if (lista[i]['Marca'] == lista[j]['Marca']):
                if (lista[i]['Precio'] < lista[j]['Precio']):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else: 
                if (lista[i]['Marca'] > lista[j]['Marca']):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    for insumo in lista:
        print("Marca: ", insumo["Marca"], "|", "Precio: ", insumo["Precio"])

marcas_iguales_por_precio(insumos)


# 6. Realizar compras: Permite realizar compras de productos. El usuario
# ingresa una marca y se muestran todos los productos disponibles de
# esa marca. Luego, el usuario elige un producto y la cantidad deseada.
# Esta acción se repite hasta que el usuario decida finalizar la compra.
# Al finalizar, se muestra el total de la compra y se genera un archivo
# TXT con la factura de la compra, incluyendo cantidad, producto,
# subtotal y el total de la compra.



# 7. Guardar en formato JSON: Genera un archivo JSON con todos los
# productos cuyo nombre contiene la palabra "Alimento".

# 8. Leer desde formato JSON: Permite mostrar un listado de los insumos
# guardados en el archivo JSON generado en la opción anterior.

# 9. Actualizar precios: Aplica un aumento del 8.4% a todos los
# productos, utilizando la función map. Los productos actualizados se
# guardan en el archivo "Insumos.csv".

# 10. Salir del programa
# Nota: Utilizar las funciones filter y reduce cuando sea necesario.


def menu():
    print("""
        ***Menu de Opciones***
        -----------------------------------------
        1 - Cargar datos:
        2 - Mostrar marcas y cantidad de productos:
        3 - Mostrar marcas y precio:
        
        """)
    opcion = input("Ingrese opcion: ")
    return opcion

def resultados():
    match(menu()):
        case "1":
            cargar_datos()
        
        case "2":
            lista_cantidad_por_marca()
        
        case "3":
            lista_insumos_marca()
        

