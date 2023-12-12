# lista  = ["Bautista", "Ramiro", "Laura", "Jose", "Lucia"]

# def ordenar_lista(lista:list, ascendente = True):
#     tam = len(lista)
#     for i in range(tam -1):
#         for j in range(i+1, tam):
#             if(ascendente and lista[i] > lista[j] or not ascendente and lista[i] < lista[j]):
#                 aux = lista[i]
#                 lista[i] = lista[j]
#                 lista[j] = aux
#     return aux

# print(ordenar_lista(lista, True))


# tam = len(lista)
# #Para ordenar lista

# print(lista)

# for i in range (tam - 1):
#     # print("i: ", i)
#     for j in range(i + 1, tam):
#         # print("j: ", j)
#         if(lista[i] >  lista[j]): # > ordena ascendente, < ordena descendente
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux

# print(lista)

# lista = [3, 6, 5, 8, 12, 3, 21, 5, 17]
# tam = len(lista)
# #Para ordenar lista

# print(lista)

# for i in range (tam - 1):
#     # print("i: ", i)
#     for j in range(i + 1, tam):
#         # print("j: ", j)
#         if(lista[i] < lista[j]): # > ordena ascendente, < ordena descendente
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux

# print(lista)

import json
with open("Desafio_Stark\\data_stark.json") as file:
    lista = json.load(file)

    tam = len(lista)

    for i in range (tam - 1):
        for j in range(i + 1, tam):      
            if(lista[i] > lista[j]): # > ordena ascendente, < ordena descendente
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


