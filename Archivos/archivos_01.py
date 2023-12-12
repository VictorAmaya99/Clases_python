import re 

#Para agregar a una lista
lista = []
with open("archivos\\carta.txt", "r") as file:
    # linea = file.readline()
    # lista.append(linea.replace("\n", ""))

#Para recorrer la lista
    #for linea in file.readlines(): tambien funciona:
    for linea in file:
        lista.append(linea.replace("\n", ""))

 
print(lista)
    


# print(lineas)

# lineas = file.readline()
# print(lineas)
# lineas = file.readline()
# print(lineas)

#file.close() 
 
#Se puede recorrer con un for despues del cierre4

# for linea in lineas:
#     print(linea)
    
#Para acceder a la lista por el indice
# for i in range(len(lineas)):
#     print(lineas[i])
    
#para quitar el \n del final
# [for i in range(len(lineas)): 
#     lineas[i] = lineas[i].replace("\n", "")
    # lineas[i] = lineas[i].strip("\n")
 
#print(lineas)

