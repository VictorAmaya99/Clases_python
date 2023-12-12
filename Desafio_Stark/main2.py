from data_stark import *

#from modulo_funciones import *



# Desafío #02: (con biblioteca propia: stark_biblioteca)
# En base a lo resuelto en el desafío #00, deberás mejorar la calidad de tus funciones.
# Es por ello que te proponemos lo siguiente:
# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
# escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
# un string, etc y que contendrá) y que es lo que retorna la función!
# 0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista
# de héroes. La función deberá:
# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
# las keys que representan datos numéricos)
# ● Validar primero que el tipo de dato no sea del tipo al cual será
# casteado. Por ejemplo si una key debería ser entero (ejemplo edad)
# verificar antes que no se encuentre ya en ese tipo de dato.
# ● Si al menos un dato fue modificado, la función deberá imprimir como
# mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
# ● Validar que la lista de héroes no esté vacía para realizar sus acciones,
# caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”

# 1.1. Crear la función 'obtener_nombre' la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y devolverá un string el cual
# contenga su nombre formateado de la siguiente manera:
# Nombre: Howard the Duck

def obtener_nombre(heroe:dict):
    for heroe in lista_personajes:
        dato_nombre = heroe["nombre"]
        print(f"nombre: {dato_nombre}")

obtener_nombre(lista_personajes)
    
print("--------------------------------------")


# 1.2. Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y
# deberá imprimirlo en la consola. La función no tendrá retorno.

def imprimir_dato(key:str):
    for heroe in lista_personajes:
        dato = heroe[key]
        print(dato)
        
imprimir_dato("color_ojos")

print("------------------------------------")

# 1.3. Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por
# parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las
# funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía

def stark_imprimir_nombres_heroes(heroe:list)->list:
    for heroe in lista_personajes:
        dato = heroe["nombre"]
        print(dato)
        
stark_imprimir_nombres_heroes(lista_personajes)
    
print("-------------------------------------------")
    
# correspondientes
# para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 1 del desafío #00

# 2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
# diccionario el cual representara a un héroe y una key (string) la cual
# representará el dato que se desea obtener.
# ● La función deberá devolver un string el cual contenga el nombre y dato
# (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
# CUALQUIER OTRO DATO.
# ● El string resultante debe estar formateado de la siguiente manera:
# (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500

def obtener_nombre_y_dato(heroe:dict, key:str)->None:
    for heroe in lista_personajes:
        dato_nombre = heroe["nombre"]
        dato_key = heroe[key]
        print(f"Nombre: {dato_nombre} | {dato_key}")

obtener_nombre_y_dato(lista_personajes, "color_ojos")

print("--------------------------------------")

# 3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por
# parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y
# alturas USANDO la función creada en el punto 2. Validar que la lista de héroes
# no esté vacía para realizar sus acciones, caso contrario no hará nada y
# retornara -1.
# Con este se resuelve el Ej 2 del desafío #00

def stark_imprimir_nombres_alturas(heroe:dict, altura:float)->None:
    for heroe in lista_personajes:
        dato_nombre = heroe["nombre"]
        dato_altura = altura["altura"]
        print("***Altura***")
        print(f"Nombre: {dato_nombre}  | Altura: {dato_altura}")

obtener_nombre_y_dato(lista_personajes, "altura")

print("--------------------------------------")
    

    
# 4.1. Crear la función 'calcular_max' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más alto.
# Ejemplo de llamada:
# calcular_max(lista, 'edad')

#def calcular_max(heroe:list, key:str)->None:
    

def calcular_max(heroe:list, key:str)->None:
    primer_heroe = lista_personajes[0]
    valor = float(primer_heroe[key])
    nombre = primer_heroe['nombre']
    for heroe in lista_personajes:
        valor_heroe = float(heroe[key])
        nombre_heroe = heroe['nombre']
        if valor_heroe > valor:
            valor = valor_heroe
            nombre = nombre_heroe
    return f"El heroe con calculo mas alto en {key}, con un valor de: {valor}, es: {nombre}, "

print(calcular_max(lista_personajes, "fuerza"))

print("------------------------------------------------")

# 4.2. Crear la función 'calcular_min' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más bajo.
# Ejemplo de llamada:
# calcular_min(lista, 'edad')

def calcular_min(heroe:list, key:str)->None:
    primer_heroe = lista_personajes[-1]
    valor = float(primer_heroe[key])
    nombre = primer_heroe['nombre']
    for heroe in lista_personajes:
        valor_heroe = float(heroe[key])
        nombre_heroe = heroe['nombre']
        if valor_heroe < valor:
            valor = valor_heroe
            nombre = nombre_heroe
    return f"El heroe con calculo mas bajo en {key}, con un valor de: {valor}, es: {nombre}, "

print(calcular_min(lista_personajes , "altura"))

print("-------------------------------------------------------")

# correspondientes

# 4.3. Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar los
# valores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# La función deberá retornar el héroe que cumpla con la condición pedida.
# Reutilizar las funciones hechas en los puntos 4.1 y 4.2
# Ejemplo de llamada:
# calcular_max_min_dato(lista, "maximo", "edad")

def calcular_max_min_dato(heroe:list, value:str, key:str)->list:
    primer_heroe = lista_personajes[0]
    valor = float(primer_heroe[key])
    nombre = primer_heroe['nombre']
    for heroe in lista_personajes:
        valor_heroe = float(heroe[key])
        nombre_heroe = heroe['nombre']
        if value == "maximo" and valor_heroe > valor:
            valor = valor_heroe
            nombre = nombre_heroe
        elif value == "minimo" and valor_heroe < valor:
            valor = valor_heroe
            nombre = nombre_heroe
    return f"El heroe con calculo  {value} en {key} con {valor}, es: {nombre}, "

print(calcular_max_min_dato(lista_personajes , "maximo", "peso"))

print("---------------------------------------------------------------")
       

# 4.4. Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres
# parámetros:
# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar los
# valores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
# La función deberá obtener el héroe que cumpla dichas condiciones, imprimir
# su nombre y el valor calculado. Reutilizar las funciones de los puntos:
# punto 1.2, punto: 2 y punto 4.3
# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara -1.
# Ejemplo de llamada:
# stark_calcular_imprimir_heroe (lista, "maximo", "edad")
# Ejemplo de salida:
# Mayor altura: Nombre: Howard the Duck | altura: 79.34

def calcular_max_min_dato(heroe:list, value:str, key:str)->None:
    primer_heroe = lista_personajes[0]
    valor = float(primer_heroe[key])
    nombre = primer_heroe['nombre']
    for heroe in lista_personajes:
        valor_heroe = float(heroe[key])
        nombre_heroe = heroe['nombre']
        if value == "maximo" and valor_heroe > valor:
            valor = valor_heroe
            nombre = nombre_heroe
        elif value == "minimo" and valor_heroe < valor:
            valor = valor_heroe
            nombre = nombre_heroe
    return f"Nombre: {nombre} | {key}: {valor}"

print(calcular_max_min_dato(lista_personajes , "maximo", "peso"))

print("---------------------------------------------------------------")

# 5.1. Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una
# lista de héroes y un string que representara el dato/key de los héroes que se
# requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un
# diccionario vacío antes de hacer la suma. La función deberá retorna la suma
# de todos los datos según la key pasada por parámetro

def sumar_dato_heroe(heroe:list, key: str)->list:
    acumulador = 0
    for heroe in lista_personajes:
        acumulador += float(heroe[key])
    return f"la suma de {key} es: {acumulador}"

print(sumar_dato_heroe(lista_personajes, "peso"))

print("---------------------------------------------")

# 5.2. Crear la función ‘dividir’ la cual recibirá como parámetro dos números
# (dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo,
# retornar 0, caso contrario realizar la división entre los parámetros y retornar el
# resultado

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("0")
    else:
        print(resultado)

dividir(15, 3)

print("----------------------------------------------------")
        

# 5.3. Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una
# lista de héroes y un string que representa el dato del héroe que se requiere
# calcular el promedio. La función debe retornar el promedio del dato pasado
# por parámetro
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 5.1 y 5.2

def calcular_promedio(heroe:list, key:str):
    acumulador = 0
    contador = 0
    for heroe in lista_personajes:
        acumulador += float(heroe[key])
        contador += 1
    
    promedio = acumulador / contador 
    
    print(f"el promedio de: {key} es:", promedio)
    
calcular_promedio(lista_personajes, "altura")
    
print("-------------------------------------")


# 5.4. Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá
# una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la
# altura promedio. Validar que la lista de héroes no esté vacía para realizar sus
# acciones, caso contrario no hará nada y retornara -1.
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y
# 5.3
# Con este se resuelve el Ej 5 del desafío #00

def stark_calcular_imprimir_promedio(heroe:list):
    acumulador = 0
    contador = 0

    for heroe in lista_personajes:
        acumulador += float(heroe["altura"])
        contador += 1

    promedio_altura = acumulador / contador #len(lista_personajes)    

    print("la suma de la altura es: {}".format(acumulador))
    print("El promedio de estatura es: ", promedio_altura)

stark_calcular_imprimir_promedio(lista_personajes)

print("-----------------------------------")

# 
# 6.1. Crear la función "imprimir_menu" que imprima el menú de opciones por
# pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se
# deberá reutilizar la función antes creada encargada de imprimir un string (1.2)

def imprimir_menu():
    print("""
        ***Menu de Opciones***
        -----------------------------------------
        1 - Cargar lista:
        2 - Mostrar personaje mas alto
        3 - Mostrar personaje mas bajo
        4 - Mostrar promedio de altura
        5 - Mostrar personaje con mas peso
        6 - Mostrar personaje con menos peso
        7 - Mostrar heroes masculinos
        8 - Mostrar heroes femeninos
        9 - Mostrar heroe masculino mas alto
        10 - Mostrar heroe femenino mas alto
        11 - Mostar heroe masculino mas bajo
        12 - Mostrar heroe femenino mas bajo
        13 - Mostrar promedio de altura de heroes masculinos
        14 - Mostrar promedio de altura de heroes femeninos
        15 - Tipo color de pelo de superheroes
        16 - Tipo color de ojos de superheroes
        17 - Tipo de inteligencia de superheroes
        """)
    opcion = input("Ingrese opcion: ")
    return opcion

print(imprimir_menu())

print("-----------------------------------------------------------------------")

# 6.2. Crear la función “validar_entero” la cual recibirá por parámetro un string de
# número el cual deberá verificar que sea sea un string conformado únicamente
# por dígitos. Retornara True en caso de serlo, False caso contrario

def validar_entero(numero:str):
    if(numero.isnumeric()):
        numero = int(numero)
        print("True")
    else:
        print("False")

validar_entero("hola")

print("----------------------------------------------------------------------")

# 6.3. Crear la función 'stark_menu_principal' la cual se encargará de imprimir el
# menú de opciones y le pedirá al usuario que ingrese el número de una de las
# opciones elegidas y deberá validarlo. En caso de ser correcto dicho número,
# lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las
# funciones del ejercicio 6.1 y 6.2

# 7. Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de
# héroes y se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con
# python 3.10+). Debe informar por consola en caso de seleccionar una opción

# correspondientes
# incorrecta y volver a pedir el dato al usuario. Reutilizar las funciones con
# prefijo 'stark_' donde crea correspondiente.
