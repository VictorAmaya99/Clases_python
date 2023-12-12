# Desafío #00:

# A. Analizar detenidamente el set de datos
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener


# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

from data_stark import *

from modulo_funciones import *

#print(resultados())



def obtener_nombre(heroe:dict)->None:
    print(f"nombre: {heroe['nombre']}")
    

for heroe in lista_personajes:
    obtener_nombre(heroe)
    
        
# def mostrar_heroe_fila(heroe: dict) -> None:
#     print(f"{heroe['nombre']:15s}     {heroe['identidad']:28s}     {heroe['empresa']}     
#           {heroe['altura']:.2f}      {heroe['peso']:.2f}      {heroe['genero']:^8s}     
#           {heroe['color_ojos']:21s}     {heroe['color_pelo']:15s}    {heroe['fuerza']:5s}      
#           {heroe['inteligencia']}")

# for heroe in lista_personajes:
#         mostrar_heroe_fila(heroe)



# print(f"""" Nombre:{heroe['nombre']}
#   Identidad:{heroe['identidad']}
#   Empresa:{heroe['empresa']}
#   Altura:{heroe['altura']}
#   Peso:{heroe['peso']}
#   Genero:{heroe['genero']}
#   Color_ojos:{heroe['color_ojos']}
#   Color_pelo:{heroe['color_pelo']}
#   Fuerza:{heroe['fuerza']}
#   Inteligencia:{heroe['inteligencia']}""")



def mostrar_lista(lista:list, title:str)->None:
    print(f"     ***{title}***    ")
    for item in lista:
        print(item)
    

def listar_heroes(lista:list)->None:
    print("                          Lista Heroes                   ")
    print("Nombre                 Indentidad                       Empresa         Altura      Peso        Genero     Color_ojos            Color_pelo         Fuerza         Inteligencia")
    for heroe in lista:
        mostrar_heroe_fila(heroe)

def mostrar_heroe_fila(heroe: dict) -> None:
    print(f"{heroe['nombre']:15s}     {heroe['identidad']:28s}     {heroe['empresa']}     {heroe['altura']:.2f}      {heroe['peso']:.2f}      {heroe['genero']:^8s}     {heroe['color_ojos']:21s}     {heroe['color_pelo']:15s}    {heroe['fuerza']:5s}      {heroe['inteligencia']}")

    for heroe in lista_personajes:
         mostrar_heroe_fila(heroe)

def mostrar_heroe(heroe:dict)->None:
    print(f"""" Nombre:{heroe['nombre']}
  Identidad:{heroe['identidad']}
  Empresa:{heroe['empresa']}
  Altura:{heroe['altura']}
  Peso:{heroe['peso']}
  Genero:{heroe['genero']}
  Color_ojos:{heroe['color_ojos']}
  Color_pelo:{heroe['color_pelo']}
  Fuerza:{heroe['fuerza']}
  Inteligencia:{heroe['inteligencia']}""")
    
def filtrar_heroes(lista:list, key:str, value:str)->list:
    lista_filtrada = []
    for heroe in lista:
        if(heroe[key] == value):
            lista_filtrada.append(heroe)
    return lista_filtrada

def proyectar_heroe(lista:list, key:str, repe:bool=False)->list:
    lista_filtrada = []
    for heroe in lista:
        lista_filtrada.append(heroe[key])
    if(not repe):
        lista_aux = []
        for item in lista_filtrada:
            if(not esta_en_lista(lista_aux, item)):
                lista_aux.append(item)
            lista_filtrada = lista_aux
    return lista_filtrada

def quitar_repetidos(lista:list)->list:
    lista_sin_repe = []
    for item in lista:
        if(not esta_en_lista(lista_sin_repe, item)):
            lista_sin_repe.append(item)
    return lista_sin_repe



#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
lista_heroes_masculino = filtrar_heroes(lista_personajes, "genero", "M")
nombres_masculinos = proyectar_heroe(lista_heroes_masculino, "nombre")
mostrar_lista(nombres_masculinos, "Nombres heroes masculinos")


l = proyectar_heroe(lista_personajes, "color_ojos")
mostrar_lista(l, "Lista color de ojos")

lista = proyectar_heroe(lista_personajes, "color_pelo", False)
mostrar_lista(lista, "lista con repetidos")

#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
lista_color_ojos = filtrar_heroes(lista_personajes, "color_ojos", "Blue")
# color_ojos = proyectar_heroe(lista_color_ojos, "nombre")
mostrar_lista = (lista_color_ojos, "tipo de color de ojos")

print(lista_color_ojos)
