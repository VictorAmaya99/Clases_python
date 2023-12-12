# 3-Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
# de memoria es la que mas ocurrencias tiene dentro de esa lista.

lista = []

seguir = "si"

while seguir == "si":
    
    while True:
        lista_numeros = input("Ingrese un numero: ")
        if(lista_numeros.isdigit()):
            lista_numeros = int(lista_numeros)
            break
        else:
            print("Eso no es un numero")
    print(lista_numeros)
    lista.append(lista_numeros)
           
    seguir = input("Desea continuar: ")


print(lista)