lista = [23, 21, 45, 33, 78]

numero_buscado = int(input("Ingerse numero a buscar: "))
# flag_esta = False

# for numero in lista:
#     if (numero == numero_buscado):
#         flag_esta = True
#         break
# if flag_esta:
#     print("El numero esta en la lista")
# else:
#         print("El numero no esta en la lista")

## Usando una variable indice

indice = -1

for i in range(len(lista)):
    if(lista[i] == numero_buscado):
        indice = i
        break

if indice != -1:
    print("El numero esta en en el indice{indice}")
else:
    print("El numero no esta en el indice")