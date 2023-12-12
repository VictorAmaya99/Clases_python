
lista = ["Primer linea\n", "Segunda linea\n", "Tercera lineassssss\n"]

#Esto es mas claro usar with as
with open("archivos\\carta2.txt", "w") as file:
    file.writelines(lista)


# file.write("Hola esto es un nuervo archivo\n")
# file.write("Hola esto es un nuervo archivo\n")
# file.write("Hola esto es un nuervo archivo\n")
# file.write("Hola esto es un nuervo archivo\n")



# print(file)

#file.close()

