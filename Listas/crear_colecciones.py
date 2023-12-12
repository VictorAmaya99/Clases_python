# lista = []

# for i in range (5):
#     numero = int(input("Ingrese un numero: "))
#     lista.append(numero)
    
# for i in range(len(lista)): primer opcion
#     print(lista[i])

# for numero in lista:    #segundo opcion mas facil de escribir
#     print(numero)
    
#Para informar la suma

# acumulador = 0

# for numero in lista:
#     acumulador += numero

# print("La suma de los numeros ingresados es {}".format(acumulador))

# #Para calcular el promedio

# promedio = acumulador / 5
# print(promedio)

##Para cambiar tamaño o cantidad del valor de una variable

lista = []
tam = 7             #El valor puede ser cambiado
acumulador = 0
contador = 0

for i in range(tam):
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)
    
for numero in lista:
    print(numero)
    
# for numero in lista:
#      acumulador += numero
# print("la suma da: {}".format(acumulador))

## Para sacar promedio1

# promedio = acumulador / len(lista)
# print(promedio)

## Se puede usar tambien un contador
for numero in lista:
    acumulador += numero
    contador += 1
print("La suma es: {}".format(acumulador))
    
promedio = acumulador / contador
print("El promedio es: ",promedio)
    
    
