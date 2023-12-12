from data import personas
# # print(personas)

# #Para mostrar solo nombres
# for persona in personas:
#     print(persona["nombre"])

## Para mostrar el de mayor edad
# flag = True
# mayor_edad = None

# for persona in personas:
#     if flag or persona["edad"] > mayor_edad:
#         mayor_edad = persona["edad"]
#         flag = False
# print("Edad mayor:{}".format(mayor_edad))

# #Para mostrar el nombre de la persona de mayor edad

# persona_mayor = personas[0]

# for persona in personas:
#     if persona["edad"] > persona_mayor["edad"]:
#         persona_mayor = persona

# print(persona_mayor)

# flag = True
# menor_edad = None

# for persona in personas:
#     if flag or persona["edad"] < menor_edad:
#         menor_edad = persona["edad"]
#         flag = False
# print("Edad menor:{}".format(menor_edad))

# #Para mostrar el nombre de la persona de mayor edad

# persona_menor = personas[0]

# for persona in personas:
#     if persona["edad"] < persona_menor["edad"]:
#         persona_menor = persona

# print(persona_menor)

##para saber cuales son las personas de mayor edad, y no muestre solo una
# for persona in personas:
#     if persona["edad"] == mayor_edad:
#         print(persona)

# flag = True
# mayor_edad = None
# nombre_mayor_edad = None

# lista = [23, 21, 45, 33, 78]
# tam = 10

# for i in range(5):
#     numero = int(input("Ingrese un numero: "))
#     lista.append(numero)

# numero_buscado = int(input("Ingrese numero a buscar: "))

# print()


    
# acumulador = 0

# for numero in lista:
#     acumulador += numero
    
# promedio = acumulador / len(lista)

#print("El promedio de los numero ingresados es{}".format(promedio))

############################################################################################################

# 1. Crear un diccionario que contenga los nombres y edades de 5 personas. Luego
# imprimir por pantalla el nombre y la edad de cada persona.

# personas = [
#     {"nombre": "Bautista", "edad": 4},
#     {"nombre": "Manuel", "edad": 28},
#     {"nombre": "Andre", "edad": 27},
#     {"nombre": "Josefina", "edad": 35},
#     {"nombre": "Libertad", "edad": 68}]

# for nombre in personas:
#     print(nombre["nombre"])

###########################################################################################################################
    
# 2. Crear un diccionario que contenga los nombres de paises y sus capitales (máximo 10
# paises y 10 capitales). Pedirle al usuario que ingrese el nombre del pais e imprimir por
# pantalla el nombre de la capital si existe en el diccionario. De lo contrario informarlo.

# paises = [{"pais": "peru", "capital": "lima"},
#           {"pais": "argentina", "capital": "buenos aires"},
#           {"pais": "paraguay", "capital": "asuncion"},
#           {"pais": "españa", "capital": "madrid"},
#           {"pais": "alemania", "capital": "berlin"},
#           {"pais": "italia", "capital": "roma"},
#           {"pais": "korea", "capital": "seul"},
#           {"pais": "japon", "capital": "tokio"},
#           {"pais": "india", "capital": "nueva delhi"},
#           {"pais": "egipto", "capital": "cairo"}]

import os

from data_datos import paises


os.system("cls")
pais_buscado = input("Ingresar pais a buscar: ")
flag_esta = False

for pais in paises:
    
    if pais["pais"] == pais_buscado:
        print("la capital es:" , pais["capital"])
        flag_esta = True
        break
    
       
if flag_esta:
    print("El pais esta en la lista")
else:
    print("El pais no esta en la lista")
    
###############################################################################################################################

# 3. Crear un diccionario que contenga los nombres de 10 frutas y su precio en dolares.
# Pedir al usuario que ingrese el nombre de una fruta y luego imprimir en pantalla su
# precio correspondiente en pesos.

# 4. Crear un diccionario que contenga los nombres de 5 animales y la cantidad de patas
# que tienen. Pedir al usuario que ingrese el nombre del animal e imprimir en pantalla la
# cantidad de patas correspondiente.

# 5. Crear un diccionario que contenga los nombres de 20 estudiantes y sus respectivas
# notas en un examen. Luego imprimir el nombre del estudiante con la nota más alta.

# 6. Rehacer los primeros 5 ejercicios pero sin hardcodear los diccionarios, es decir, el
# diccionario debe empezar vacio y deberán cargar las claves y valores del diccionario
# por consola.

# Desde ahora en más, los diccionarios deberian empezar vacíos.
# 7. Crear un diccionario que contenga los nombres, edades, alturas (en metros), pesos (en
# kilogramos) y ciudades de un numero indeterminados de personas. Luego calcular el
# indice de masa corporal (IMC) de cada persona y agregarlo al diccionario. Finalmente,
# imprimir en pantalla los nombres de las personas junto con su ciudad y si IMC
# (redondeando a 2 decimales).

# 8. Crear un diccionario que contenga los nombres, edades, salario por día, días trabajados
# de 10 empleados. Luego, calcular el salario total de cada empleado y agregarlo al
# diccionario. Finalmente, imprimir en consola los nombres de los empleados junto con
# la edad y el salario total.

# 9. Crear un diccionario que contenga los nombres, edades, fechas de nacimiento,
# numeros de telefono y correos electrónicos de un numero indeterminado de personas.
# Luego, concatenar la fecha de nacimiento y el número de teléfono de cada persona con
# el formato “11-1111-1111 – dd/mm/aaaa” y agregarlo al diccionario (usar un string
# interpolado con format para hacerlo más facil). Finalmente imprimir en consola el
# nombre, correo electrónico y los datos concatenados.

# 10. Crear un diccionario que contenga los nombres, edades, alturas (en centímetros) y
# géneros de 10 personas. Luego, convertir las alturas de centímetros a pies y pulgadas
# sabiendo que un pie son 30.48 cm y 1 pulgada son 2.54 cm) y agregar los datos al
# diccionario. Finalmente, imprimir en consola los nombres de las personas con su
# genero y su altura en pies y pulgadas.

# 11. Crear un diccionario que contenga los nombres, edades, saldos en cuentas bancarias y
# un codigo de cliente (debe ser un string de 8 caracteres alfanumérico) y un porcentaje
# de impuesto a aplicar. Imprimir por consola el codigo del cliente y el balance final de la
# cuenta.

# Listas de diccionarios.
# 12. Crear una lista de diccionarios que contenga información sobre 5 libros, incluyendo
# título, autor, editorial, año de publicación, y género. Luego, pedir al usuario que ingrese
# un género y mostrar en pantalla todos los títulos de ese género con todos los datos.

# 13. Crear una lista de diccionarios que contenga información sobre 5 películas, incluyendo
# título, director, año de estreno, género y duración en minutos. Luego, pedir al usuario
# que ingrese una duración máxima y mostrar por consola los títulos de las películas que
# no excedan esa duración ordenado alfabéticamente por nombre de la pelicula (pueden
# usar listas auxiliares para guardar datos).

# 14. Crear una lista de diccionarios que contenga la información de 10 canciones incluyendo
# nombre del artista, titulo de la cancion, álbum al que pertenece, año de lanzamiento y
# duración en segundos. Luego, pedir al usuario que ingrese una duración mínima y
# mostrar por consola de forma diferenciada las canciones que tengan menor tiempo y
# mayor tiempo con respecto al ingresado por el usuario.

# 15. Crear una aplicación que permita a los usuarios agregar y buscar películas de una lista
# de diccionarios. Cada diccionario debe contener información sobre una película,
# incluyendo su titulo, director, año de estreno, genero, y duración en minutos. Al iniciar
# la aplicación, se debe mostrar un menú que permita al usuario elegir entre agregar una
# película o buscar una película por título. Si el usuario elige agregar una película, se
# deben pedir los datos por consola y agregarlos a la lista de diccionarios. Si el usuario
# elige buscar una película por título, se le debe pedir el nombre de la película que busco
# por consola y mostrar en pantalla la información completa de la película si existe o un
# mensaje indicando que la película no se encuentra en el listado.

# 16. Crear una aplicación que permita a los usuarios agregar o buscar libros de una lista de
# diccionarios. Cada diccionario dentro de la lista debe contener los datos de un libro
# incluyendo su titulo, autor, editorial, año de publicación, genero, y número de páginas.
# Al iniciar la aplicación se deberá mostrar el menú de opciones donde se le permita al
# usuario elegir si quiere buscar un libro por autor o agregar un libro a la lista de libros. Si
# el usuario elige buscar un libro, se debe pedir el nombre del autor que desea y deberán
# mostrar todos los libros de ese autor con sus datos correspondientes ordenados
# alfabéticamente por título. Si se elige agregar un libro, se deberán pedir todos los datos
# y guardaros en un nuevo diccionario dentro de la lista.