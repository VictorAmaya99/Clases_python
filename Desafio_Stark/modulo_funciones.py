from data_stark import *

lista = []

for heroe in lista_personajes:
    lista.append(heroe.copy())

def mostrar_heroe_fila(heroe: dict) -> None:
    print(f"{heroe['nombre']:15s}     {heroe['identidad']:28s}     {heroe['empresa']}     {heroe['altura']:.2f}      {heroe['peso']:.2f}      {heroe['genero']:^8s}     {heroe['color_ojos']:21s}     {heroe['color_pelo']:15s}    {heroe['fuerza']:5s}      {heroe['inteligencia']}")

    for heroe in lista_personajes:
        mostrar_heroe_fila(heroe)

def lista():
    for nombre in lista_personajes:
        print(f"{nombre['nombre']:20s}     {nombre['altura']:5.2f}           {nombre['peso']:5.2f}")

def personaje_mas_alto():
    flag_alto = False
    mas_alto = None
    nombre_mas_alto = None

    for personaje in lista_personajes:
        if flag_alto == False or personaje["altura"] > mas_alto:
            mas_alto = personaje["altura"]
            nombre_mas_alto = personaje["nombre"]
            flag_alto = True

    print("mayor altura: {}".format(mas_alto))
    print("El nombre del heroe mas alto es: ", nombre_mas_alto)
    
def personaje_mas_bajo():
    flag_bajo = False
    mas_bajo = None
    nombre_mas_bajo = None

    for personaje in lista_personajes:
        if flag_bajo == False or personaje["altura"] < mas_bajo:
            mas_bajo = personaje["altura"]
            nombre_mas_bajo = personaje["nombre"]
            flag_bajo = True
    
    print("menor altura:{}".format(mas_bajo))
    print("El nombre del heroe mas bajo es: ", nombre_mas_bajo)
    
def promedio_altura():
    acumulador = 0

    for altura in lista_personajes:
        acumulador += float(altura["altura"])

    promedio_altura = acumulador / len(lista_personajes)    

    print("la suma de la altura es: {}".format(acumulador))
    print("El promedio de estatura es: ", promedio_altura)
    
def personaje_mas_peso():
    flag = True
    mayor_peso = None
    nombre_peso_mayor = None

    for personaje in lista_personajes:
        if flag or personaje["peso"] > mayor_peso:
            mayor_peso = personaje["peso"]
            nombre_peso_mayor = personaje["nombre"]
            flag = False
    
    print("mayor peso: {}".format(mayor_peso))
    print("El nombre del personaje con mayor peso es: ", nombre_peso_mayor)


def personaje_menos_peso():
    flag = True
    menor_peso = None
    nombre_peso_menor = None

    for personaje in lista_personajes:
        if flag or personaje["peso"] < menor_peso:
            menor_peso = personaje["peso"]
            nombre_peso_menor = personaje["nombre"]
            flag = False
    
    print("menor peso: {}".format(menor_peso))
    print("El nombre del personaje con menor peso es: ", nombre_peso_menor)
    

# def genero_masculino():
#     for personaje in lista_personajes:
#         if personaje["genero"] == "M":
#             print(f"{personaje['nombre']:20s}     {personaje['genero']}     {personaje['altura']}")
    
# def genero_femenino():
#     for personaje in lista_personajes:
#         if personaje["genero"] == "F":
#             print(f"{personaje['nombre']:20s}     {personaje['genero']}     {personaje['altura']}")
    
def personaje_mas_alto_masculino():
    flag_alto_masculino = False
    mas_alto_masculino = None
    nombre_mas_alto_masculino = None
    
    for personaje in lista_personajes:
        if flag_alto_masculino == False or personaje["genero"] == "M" and personaje["altura"] > mas_alto_masculino:
            mas_alto_masculino = personaje["altura"]
            nombre_mas_alto_masculino = personaje["nombre"]
            flag_alto_masculino = True

    print("mayor altura: {}".format(mas_alto_masculino))
    print(f"El nombre del heroe masculino mas alto es: ", nombre_mas_alto_masculino)
    
def personaje_mas_alto_femenino():
    flag_alto_femenino = False
    mas_alto_femenino = None
    nombre_mas_alto_femenino = None
    
    for personaje in lista_personajes:
        if flag_alto_femenino == False or personaje["genero"] == "F" and personaje["altura"] > mas_alto_femenino:
            mas_alto_femenino = personaje["altura"]
            nombre_mas_alto_femenino = personaje["nombre"]
            flag_alto_femenino = True

    print("mayor altura: {}".format(mas_alto_femenino))
    print(f"El nombre del heroe femenino mas alto es: ", nombre_mas_alto_femenino)
    
def personaje_mas_bajo_masculino():
    primer_personaje = lista_personajes[-1]
    genero = primer_personaje["genero"]
    altura = primer_personaje["altura"]
    nombre = primer_personaje["nombre"]
    for personaje in lista_personajes:
        genero_personaje = personaje["genero"]
        altura_personaje = personaje["altura"]
        nombre_personaje = personaje["nombre"]
        if altura_personaje < altura and genero_personaje == "M":
            genero = genero_personaje
            altura = altura_personaje
            nombre = nombre_personaje
        
    print("la altura minima es:", altura)
    print("el nombre es:", nombre)
    print("El genero es: ", genero)


def personaje_mas_bajo_femenino():
    primer_personaje = lista_personajes[-1]
    genero = primer_personaje["genero"]
    altura = primer_personaje["altura"]
    nombre = primer_personaje["nombre"]
    for personaje in lista_personajes:
        genero_personaje = personaje["genero"]
        altura_personaje = personaje["altura"]
        nombre_personaje = personaje["nombre"]
        if altura_personaje < altura and genero_personaje == "F":
            genero = genero_personaje
            altura = altura_personaje
            nombre = nombre_personaje
        
    print("la altura minima es:", altura)
    print("el nombre es:", nombre)
    print("El genero es: ", genero)
    
def promedio_altura_masculino():
    primer_personaje = lista_personajes[0]
    acumulador_masculino = 0
    contador_masculino = 0
    genero = primer_personaje["genero"]
    altura = primer_personaje["altura"]
    for personaje in lista_personajes:
        genero_personaje = personaje["genero"]
        altura_personaje = personaje["altura"]
        if genero_personaje == "M":
            acumulador_masculino += float(altura_personaje)
            contador_masculino +=1

    promedio_altura = acumulador_masculino / contador_masculino
        
    print("la suma de la altura es: {}".format(acumulador_masculino))
    print("el promedio de altura masculino es: ", promedio_altura)
    
def promedio_altura_femenino():
    primer_personaje = lista_personajes[0]
    acumulador_femenino = 0
    contador_femenino = 0
    genero = primer_personaje["genero"]
    altura = primer_personaje["altura"]
    for personaje in lista_personajes:
        genero_personaje = personaje["genero"]
        altura_personaje = personaje["altura"]
        if genero_personaje == "F":
            acumulador_femenino += float(altura_personaje)
            contador_femenino +=1

    promedio_altura = acumulador_femenino / contador_femenino
        
    print("la suma de la altura es: {}".format(acumulador_femenino))
    print("el promedio de altura femenino es: ", promedio_altura)
    
def esta_en_lista(lista:list, item:str)->bool:
    esta = False
    for elemento in lista:
        if(elemento == item):
            esta = True
            break
    return esta

lista = []
colores = []
inteligencia = []

for heroe in lista_personajes:
    lista.append(heroe.copy())
   
# N. Listar todos los superhéroes agrupados por color de pelo. 
# Todo va dentro de una funcion
def lista_heroes_color_pelo():
    for heroe in lista:
        if not  esta_en_lista(colores, heroe["color_pelo"]):
            colores.append(heroe["color_pelo"])
        
    for color in colores:
        print("color: " + color)
        for heroe in lista:
            if(heroe["color_pelo"] == color):
                print(heroe["nombre"], heroe["color_pelo"])
            
        print("------------------------------")

lista_heroes_color_pelo()
        
# M. Listar todos los superhéroes agrupados por color de ojos.

def lista_color_ojos():
    for heroe in lista:
        if not  esta_en_lista(colores, heroe["color_ojos"]):
            colores.append(heroe["color_ojos"])
      
    for color in colores:
        print("color: " + color)
        for heroe in lista:
            if(heroe["color_ojos"] == color):
                print(heroe["nombre"], heroe["color_ojos"])
            
        print("------------------------------")


        
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

def lista_tipo_inteligencia():
    for heroe in lista:
        if not  esta_en_lista(inteligencia, heroe["inteligencia"]):
            inteligencia.append(heroe["inteligencia"])
        
    for smart in inteligencia:
        print("Inteligencia: " + smart)
        for heroe in lista:
            if(heroe["inteligencia"] == smart):
                print(heroe["nombre"], heroe["inteligencia"])
            
        print("------------------------------")

        
def mostrar_lista(lista:list, title:str)->None:
    print(f"     ***{title}***    ")
    for item in lista:
        print(item)
    
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



# def menu():
#     print("""
#         ***Menu de Opciones***
#         -----------------------------------------
#         1 - Cargar lista:
#         2 - Mostrar personaje mas alto
#         3 - Mostrar personaje mas bajo
#         4 - Mostrar promedio de altura
#         5 - Mostrar personaje con mas peso
#         6 - Mostrar personaje con menos peso
#         7 - Mostrar heroes masculinos
#         8 - Mostrar heroes femeninos
#         9 - Mostrar heroe masculino mas alto
#         10 - Mostrar heroe femenino mas alto
#         11 - Mostar heroe masculino mas bajo
#         12 - Mostrar heroe femenino mas bajo
#         13 - Mostrar promedio de altura de heroes masculinos
#         14 - Mostrar promedio de altura de heroes femeninos
#         15 - Tipo color de pelo de superheroes
#         16 - Tipo color de ojos de superheroes
#         17 - Tipo de inteligencia de superheroes
#         """)
#     opcion = input("Ingrese opcion: ")
#     return opcion
        
# def resultados():
#     match(menu()):
#         case "1":
#             print(mostrar_heroe_fila(heroe))

#         case "2":
#             print(personaje_mas_alto())
    
#         case "3":
#             print(personaje_mas_bajo())
        
#         case "4":
#             print(promedio_altura())
    
#         case "5":
#             print(personaje_mas_peso())
        
#         case "6":
#             print(personaje_menos_peso())
        
#         case "7":
#             lista_heroes_masculino = filtrar_heroes(lista_personajes, "genero", "M")
#             nombres_masculinos = proyectar_heroe(lista_heroes_masculino, "nombre")
#             mostrar_lista(nombres_masculinos, "Nombres heroes masculinos")
        
#         case "8":
#             lista_heroes_femeninos = filtrar_heroes(lista_personajes, "genero", "F")
#             nombres_femeninos = proyectar_heroe(lista_heroes_femeninos, "nombre")
#             mostrar_lista(nombres_femeninos, "Nombres heroes masculinos")
        
#         case "9":
#             print(personaje_mas_alto_masculino())
            
#         case "10":
#             print(personaje_mas_alto_femenino())
        
#         case "11":
#             print(personaje_mas_bajo_masculino())
            
#         case "12":
#             print(personaje_mas_bajo_femenino())
        
#         case "13":
#             print(promedio_altura_masculino())
        
#         case "14":
#             print(promedio_altura_femenino())
        
#         case "15":
#             print(lista_heroes_color_pelo())
            
#         case "16":
#             print(lista_color_ojos())
            
#         case "17":
#             print(lista_tipo_inteligencia())
        

